"""
Copyright (c) 2026 Voidev

This file is part of Void-Tools.

Licensed under the Void-Tools Source-Available License (VTSAL).
See the LICENSE file for details.
"""
# ============================================================================================= #
# ========== call_Moduls========== #
import json
import datetime
import os
import sys
import random
import logging
import pathlib
import math
import socket
import threading
from PySide6.QtWidgets import (QApplication,QMainWindow,QWidget,
QLineEdit,QLabel,QLayout,QBoxLayout,QTabBar,QStatusBar)
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QAction,QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
import qtawesome as qta
import requests
import bs4
import django
# ====================================================== #



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Void-Tools")
        self.setGeometry(500,500,500,500)
        














# ========== For_run_app ========== #
app = QApplication()
window = Mainwindow()
window.show()
sys.exit(app.exec())
