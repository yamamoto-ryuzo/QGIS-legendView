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
        QtOrientation = Qt.Orientation
        QtAlignment = Qt.AlignmentFlag
    except:
        # Fallback for older Qt6 versions
        QtOrientation = Qt
        QtAlignment = Qt
else:
    # Qt5 enum access
    QtOrientation = Qt
    QtAlignment = Qt

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
    'QtOrientation', 'QtAlignment',
    'QT_VERSION', 'get_qt_version', 'translate'
]
