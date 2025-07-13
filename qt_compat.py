# -*- coding: utf-8 -*-
"""
Qt5/Qt6 Compatibility Module for QGIS Plugin
Provides consistent imports for both Qt5 and Qt6 environments
"""

# Qt version detection and imports
try:
    # Try Qt6 first (QGIS 3.22+)
    from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt, pyqtSignal, QSize, QVariant
    from qgis.PyQt.QtGui import QIcon, QBrush, QPixmap, QImage, QFont
    from qgis.PyQt.QtWidgets import (QAction, QDockWidget, QTableWidget, QTableWidgetItem, 
                                     QApplication, QWidget, QHeaderView, QMessageBox, QLabel, QStyle)
    from qgis.PyQt import QtGui, QtWidgets, uic
    QT_VERSION = 6
except ImportError:
    try:
        # Fallback to Qt5 (QGIS 3.0-3.21)
        from PyQt5.QtCore import QSettings, QTranslator, QCoreApplication, Qt, pyqtSignal, QSize, QVariant
        from PyQt5.QtGui import QIcon, QBrush, QPixmap, QImage, QFont
        from PyQt5.QtWidgets import (QAction, QDockWidget, QTableWidget, QTableWidgetItem,
                                     QApplication, QWidget, QHeaderView, QMessageBox, QLabel, QStyle)
        from PyQt5 import QtGui, QtWidgets, uic
        QT_VERSION = 5
    except ImportError:
        # Last resort - try direct PyQt6
        from PyQt6.QtCore import QSettings, QTranslator, QCoreApplication, Qt, pyqtSignal, QSize, QVariant
        from PyQt6.QtGui import QIcon, QBrush, QPixmap, QImage, QFont
        from PyQt6.QtWidgets import (QAction, QDockWidget, QTableWidget, QTableWidgetItem,
                                     QApplication, QWidget, QHeaderView, QMessageBox, QLabel, QStyle)
        from PyQt6 import QtGui, QtWidgets, uic
        QT_VERSION = 6

# Qt5/Qt6 compatibility constants and functions
if QT_VERSION == 6:
    # Qt6 specific implementations
    try:
        from PyQt6.QtCore import Qt
        from PyQt6.QtWidgets import QAbstractItemView
        
        # Alignment constants for Qt6
        AlignHCenter = Qt.AlignmentFlag.AlignHCenter
        AlignVCenter = Qt.AlignmentFlag.AlignVCenter
        AlignCenter = Qt.AlignmentFlag.AlignCenter
        AlignLeft = Qt.AlignmentFlag.AlignLeft
        AlignRight = Qt.AlignmentFlag.AlignRight
        AlignTop = Qt.AlignmentFlag.AlignTop
        AlignBottom = Qt.AlignmentFlag.AlignBottom
        
        # Orientation constants for Qt6
        QtOrientation = Qt.Orientation
        
        # Widget attributes for Qt6
        WA_DeleteOnClose = Qt.WidgetAttribute.WA_DeleteOnClose
        RightDockWidgetArea = Qt.DockWidgetArea.RightDockWidgetArea
        PM_ListViewIconSize = QStyle.PixelMetric.PM_ListViewIconSize
        
        # Selection modes for Qt6
        NoSelection = QAbstractItemView.SelectionMode.NoSelection
        SingleSelection = QAbstractItemView.SelectionMode.SingleSelection
        MultiSelection = QAbstractItemView.SelectionMode.MultiSelection
        ExtendedSelection = QAbstractItemView.SelectionMode.ExtendedSelection
        ContiguousSelection = QAbstractItemView.SelectionMode.ContiguousSelection
        
        def setLabelAlignment(label):
            """Qt6 specific alignment setting"""
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        def createSymbolPreview(symbol, size):
            """Qt6 specific symbol preview creation - 95% of frame size"""
            try:
                from qgis.core import QgsSymbolLayerUtils
                # Use 95% of the available frame size for optimal display
                enhanced_size = QSize(int(size.width() * 0.95), int(size.height() * 0.95))
                return QgsSymbolLayerUtils.symbolPreviewPixmap(symbol, enhanced_size)
            except:
                from PyQt6.QtGui import QPixmap
                return QPixmap(size)
            
    except Exception as e:
        # Fallback for Qt6
        AlignHCenter = getattr(Qt, 'AlignHCenter', 0x0004)
        AlignVCenter = getattr(Qt, 'AlignVCenter', 0x0080)
        AlignCenter = getattr(Qt, 'AlignCenter', 0x0084)
        AlignLeft = getattr(Qt, 'AlignLeft', 0x0001)
        AlignRight = getattr(Qt, 'AlignRight', 0x0002)
        AlignTop = getattr(Qt, 'AlignTop', 0x0020)
        AlignBottom = getattr(Qt, 'AlignBottom', 0x0040)
        QtOrientation = getattr(Qt, 'Orientation', Qt)
        WA_DeleteOnClose = getattr(Qt, 'WA_DeleteOnClose', 0x0037)
        RightDockWidgetArea = getattr(Qt, 'RightDockWidgetArea', 0x2)
        PM_ListViewIconSize = getattr(QStyle, 'PM_ListViewIconSize', 1)
        NoSelection = 0
        SingleSelection = 1
        MultiSelection = 2
        ExtendedSelection = 3
        ContiguousSelection = 4
        
        def setLabelAlignment(label):
            """Qt6 fallback alignment setting"""
            try:
                label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            except:
                label.setAlignment(0x0004 | 0x0080)
        
        def createSymbolPreview(symbol, size):
            """Qt6 fallback symbol preview creation - 95% of frame size"""
            try:
                from qgis.core import QgsSymbolLayerUtils
                # Use 95% of the available frame size for optimal display
                enhanced_size = QSize(int(size.width() * 0.95), int(size.height() * 0.95))
                return QgsSymbolLayerUtils.symbolPreviewPixmap(symbol, enhanced_size)
            except:
                from PyQt6.QtGui import QPixmap
                return QPixmap(size)

else:
    # Qt5 specific implementations
    try:
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QAbstractItemView
        
        # Alignment constants for Qt5
        AlignHCenter = Qt.AlignHCenter
        AlignVCenter = Qt.AlignVCenter
        AlignCenter = Qt.AlignCenter
        AlignLeft = Qt.AlignLeft
        AlignRight = Qt.AlignRight
        AlignTop = Qt.AlignTop
        AlignBottom = Qt.AlignBottom
        
        # Orientation constants for Qt5
        QtOrientation = Qt
        
        # Widget attributes for Qt5
        WA_DeleteOnClose = Qt.WA_DeleteOnClose
        RightDockWidgetArea = Qt.RightDockWidgetArea
        PM_ListViewIconSize = QStyle.PM_ListViewIconSize
        
        # Selection modes for Qt5
        NoSelection = QAbstractItemView.NoSelection
        SingleSelection = QAbstractItemView.SingleSelection
        MultiSelection = QAbstractItemView.MultiSelection
        ExtendedSelection = QAbstractItemView.ExtendedSelection
        ContiguousSelection = QAbstractItemView.ContiguousSelection
        
        def setLabelAlignment(label):
            """Qt5 specific alignment setting - safe for Qt5"""
            try:
                # Use integer values for Qt5 to avoid freeze issues
                label.setAlignment(0x0004 | 0x0080)  # AlignHCenter | AlignVCenter
            except Exception as e:
                # Ultimate fallback
                pass
        
        def createSymbolPreview(symbol, size):
            """Qt5 specific symbol preview creation - 95% of frame size"""
            try:
                from qgis.core import QgsSymbolLayerUtils
                # Use 95% of the available frame size for optimal display
                enhanced_size = QSize(int(size.width() * 0.95), int(size.height() * 0.95))
                return QgsSymbolLayerUtils.symbolPreviewPixmap(symbol, enhanced_size)
            except:
                # Create empty pixmap if all fails
                from PyQt5.QtGui import QPixmap, QPainter, QBrush
                from PyQt5.QtCore import Qt
                pixmap = QPixmap(size)
                pixmap.fill(Qt.transparent)
                painter = QPainter(pixmap)
                painter.setBrush(QBrush(Qt.lightGray))
                painter.drawRect(0, 0, size.width(), size.height())
                painter.end()
                return pixmap
                
    except Exception as e:
        # Ultimate fallback for Qt5
        AlignHCenter = 0x0004
        AlignVCenter = 0x0080
        AlignCenter = 0x0084
        AlignLeft = 0x0001
        AlignRight = 0x0002
        AlignTop = 0x0020
        AlignBottom = 0x0040
        QtOrientation = None
        WA_DeleteOnClose = 0x0037
        RightDockWidgetArea = 0x2
        PM_ListViewIconSize = 1
        NoSelection = 0
        SingleSelection = 1
        MultiSelection = 2
        ExtendedSelection = 3
        ContiguousSelection = 4
        
        def setLabelAlignment(label):
            """Fallback alignment setting"""
            try:
                label.setAlignment(0x0004 | 0x0080)
            except:
                pass
        
        def createSymbolPreview(symbol, size):
            """Fallback symbol preview creation - 95% of frame size"""
            try:
                from qgis.core import QgsSymbolLayerUtils
                # Use 95% of the available frame size for optimal display
                enhanced_size = QSize(int(size.width() * 0.95), int(size.height() * 0.95))
                return QgsSymbolLayerUtils.symbolPreviewPixmap(symbol, enhanced_size)
            except:
                try:
                    from PyQt5.QtGui import QPixmap
                    return QPixmap(size)
                except:
                    from PyQt6.QtGui import QPixmap
                    return QPixmap(size)

def get_qt_version():
    """Return Qt version as integer (5 or 6)"""
    return QT_VERSION

def is_qt6():
    """Check if running Qt6"""
    return QT_VERSION == 6

def is_qt5():
    """Check if running Qt5"""
    return QT_VERSION == 5

# Translation compatibility
def translate(context, text, disambig=None):
    """Qt5/Qt6 compatible translation function"""
    try:
        return QCoreApplication.translate(context, text, disambig)
    except TypeError:
        # Qt5 style
        return QCoreApplication.translate(context, text)
    except:
        return text
