# ========== Moduls ========== #
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from ui.topbar import TopBar
from ui.desktop import Desktop
from ui.taskbar import TaskBar

from utils.functions import close_window
# ================================================== #


# ========== class Mainwindo ========== #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Void-Tools")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.central_widget.setLayout(self.main_layout)
        self.topbar = TopBar()
        self.main_layout.addWidget(self.topbar)
        self.desktop = Desktop()
        self.main_layout.addWidget(self.desktop)
        
        self.taskbar = TaskBar()
        self.main_layout.addWidget(self.taskbar)
        shortcut_esc = QShortcut(QKeySequence(Qt.Key_Escape), self)
        shortcut_esc.activated.connect(close_window)
        