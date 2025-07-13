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

# Qt5/Qt6 compatibility constants
if QT_VERSION == 6:
    # Qt6 uses different enum access
    try:
        from PyQt6.QtCore import Qt
        from PyQt6.QtWidgets import QAbstractItemView
        QtOrientation = Qt.Orientation
        QtAlignment = Qt.AlignmentFlag
        # Selection modes for Qt6
        QtSelectionMode = QAbstractItemView.SelectionMode
        NoSelection = QAbstractItemView.SelectionMode.NoSelection
        SingleSelection = QAbstractItemView.SelectionMode.SingleSelection
        MultiSelection = QAbstractItemView.SelectionMode.MultiSelection
        ExtendedSelection = QAbstractItemView.SelectionMode.ExtendedSelection
        ContiguousSelection = QAbstractItemView.SelectionMode.ContiguousSelection
        # Alignment constants for Qt6
        AlignHCenter = Qt.AlignmentFlag.AlignHCenter
        AlignVCenter = Qt.AlignmentFlag.AlignVCenter
        AlignCenter = Qt.AlignmentFlag.AlignCenter
        AlignLeft = Qt.AlignmentFlag.AlignLeft
        AlignRight = Qt.AlignmentFlag.AlignRight
        AlignTop = Qt.AlignmentFlag.AlignTop
        AlignBottom = Qt.AlignmentFlag.AlignBottom
        # Widget attributes for Qt6
        WA_DeleteOnClose = Qt.WidgetAttribute.WA_DeleteOnClose
        # Dock widget areas for Qt6
        RightDockWidgetArea = Qt.DockWidgetArea.RightDockWidgetArea
        # Pixel metrics for Qt6
        PM_ListViewIconSize = QStyle.PixelMetric.PM_ListViewIconSize
    except:
        # Fallback for older Qt6 versions
        QtOrientation = Qt
        QtAlignment = Qt
        try:
            from PyQt6.QtWidgets import QAbstractItemView
            QtSelectionMode = QAbstractItemView.SelectionMode
            NoSelection = QAbstractItemView.SelectionMode.NoSelection
            SingleSelection = QAbstractItemView.SelectionMode.SingleSelection
            MultiSelection = QAbstractItemView.SelectionMode.MultiSelection
            ExtendedSelection = QAbstractItemView.SelectionMode.ExtendedSelection
            ContiguousSelection = QAbstractItemView.SelectionMode.ContiguousSelection
            # Alignment constants fallback
            AlignHCenter = Qt.AlignHCenter if hasattr(Qt, 'AlignHCenter') else 0x0004
            AlignVCenter = Qt.AlignVCenter if hasattr(Qt, 'AlignVCenter') else 0x0080
            AlignCenter = Qt.AlignCenter if hasattr(Qt, 'AlignCenter') else 0x0084
            AlignLeft = Qt.AlignLeft if hasattr(Qt, 'AlignLeft') else 0x0001
            AlignRight = Qt.AlignRight if hasattr(Qt, 'AlignRight') else 0x0002
            AlignTop = Qt.AlignTop if hasattr(Qt, 'AlignTop') else 0x0020
            AlignBottom = Qt.AlignBottom if hasattr(Qt, 'AlignBottom') else 0x0040
            # Widget attributes fallback
            WA_DeleteOnClose = Qt.WA_DeleteOnClose if hasattr(Qt, 'WA_DeleteOnClose') else 0x0037
            # Dock widget areas fallback
            RightDockWidgetArea = Qt.RightDockWidgetArea if hasattr(Qt, 'RightDockWidgetArea') else 0x2
            # Pixel metrics fallback
            PM_ListViewIconSize = QStyle.PM_ListViewIconSize if hasattr(QStyle, 'PM_ListViewIconSize') else 1
        except:
            # Ultimate fallback
            QtSelectionMode = None
            NoSelection = 0
            SingleSelection = 1
            MultiSelection = 2
            ExtendedSelection = 3
            ContiguousSelection = 4
            # Alignment constants ultimate fallback
            AlignHCenter = 0x0004
            AlignVCenter = 0x0080
            AlignCenter = 0x0084
            AlignLeft = 0x0001
            AlignRight = 0x0002
            AlignTop = 0x0020
            AlignBottom = 0x0040
            # Widget attributes ultimate fallback
            WA_DeleteOnClose = 0x0037
            # Dock widget areas ultimate fallback
            RightDockWidgetArea = 0x2
            # Pixel metrics ultimate fallback
            PM_ListViewIconSize = 1
else:
    # Qt5 enum access
    QtOrientation = Qt
    QtAlignment = Qt
    try:
        from PyQt5.QtWidgets import QAbstractItemView
        QtSelectionMode = QAbstractItemView
        NoSelection = QAbstractItemView.NoSelection
        SingleSelection = QAbstractItemView.SingleSelection
        MultiSelection = QAbstractItemView.MultiSelection
        ExtendedSelection = QAbstractItemView.ExtendedSelection
        ContiguousSelection = QAbstractItemView.ContiguousSelection
        # Alignment constants for Qt5
        AlignHCenter = Qt.AlignHCenter
        AlignVCenter = Qt.AlignVCenter
        AlignCenter = Qt.AlignCenter
        AlignLeft = Qt.AlignLeft
        AlignRight = Qt.AlignRight
        AlignTop = Qt.AlignTop
        AlignBottom = Qt.AlignBottom
        # Widget attributes for Qt5
        WA_DeleteOnClose = Qt.WA_DeleteOnClose
        # Dock widget areas for Qt5
        RightDockWidgetArea = Qt.RightDockWidgetArea
        # Pixel metrics for Qt5
        PM_ListViewIconSize = QStyle.PM_ListViewIconSize
    except:
        # Fallback for Qt5
        QtSelectionMode = None
        NoSelection = 0
        SingleSelection = 1
        MultiSelection = 2
        ExtendedSelection = 3
        ContiguousSelection = 4
        # Alignment constants fallback for Qt5
        AlignHCenter = 0x0004
        AlignVCenter = 0x0080
        AlignCenter = 0x0084
        AlignLeft = 0x0001
        AlignRight = 0x0002
        AlignTop = 0x0020
        AlignBottom = 0x0040
        # Widget attributes fallback for Qt5
        WA_DeleteOnClose = 0x0037
        # Dock widget areas fallback for Qt5
        RightDockWidgetArea = 0x2
        # Pixel metrics fallback for Qt5
        PM_ListViewIconSize = 1

def get_qt_version():
    """Return the Qt version being used"""
    return QT_VERSION

def translate(context, message):
    """Qt5/Qt6 compatible translation function"""
    return QCoreApplication.translate(context, message)

# Export all commonly used Qt classes and functions
__all__ = [
    'QSettings', 'QTranslator', 'QCoreApplication', 'Qt', 'pyqtSignal', 'QSize', 'QVariant',
    'QIcon', 'QBrush', 'QPixmap', 'QImage', 'QFont',
    'QAction', 'QDockWidget', 'QTableWidget', 'QTableWidgetItem', 
    'QApplication', 'QWidget', 'QHeaderView', 'QMessageBox', 'QLabel', 'QStyle',
    'QtGui', 'QtWidgets', 'uic',
    'QtOrientation', 'QtAlignment', 'QtSelectionMode',
    'NoSelection', 'SingleSelection', 'MultiSelection', 'ExtendedSelection', 'ContiguousSelection',
    'AlignHCenter', 'AlignVCenter', 'AlignCenter', 'AlignLeft', 'AlignRight', 'AlignTop', 'AlignBottom',
    'WA_DeleteOnClose', 'RightDockWidgetArea', 'PM_ListViewIconSize',
    'QT_VERSION', 'get_qt_version', 'translate'
]
