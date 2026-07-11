# ========== Moduls ========== #
import qtawesome as qta

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui.Startmenu import StartMenu

from pathlib import Path
# =========================================== #

# ========== class taskbar ========== #

class TaskBar(QWidget):
    startcliked = Signal()
    def __init__(self):
        super().__init__()
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.space_left = QWidget()
        self.space_left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.space_right = QWidget()
        self.space_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        ICON_SIZE = QSize(32,32)
        self.setObjectName("taskbars")
        self.setFixedHeight(60)
        self.lay_task_app = QHBoxLayout()
        self.setLayout(self.lay_task_app)

       

        icon_terminal = qta.icon("ph.terminal-window-fill",color="white")
        icon_calc = qta.icon("ph.calculator-fill",color="white")
        icon_requests = qta.icon("fa5s.eye",color="white")
        icon_file = qta.icon("msc.file-directory",color="white")

        self.btn_app_driver = QPushButton()
        img_address = Path(__file__).resolve().parent.parent.parent
        name_img = img_address /'assets'/'icons'/'icon_3232.png'
        self.btn_app_driver.setIcon(QIcon(str(name_img)))
        ICON_SIZE_DRI = QSize(100,90)
        self.btn_app_driver.setIconSize(ICON_SIZE_DRI)
        self.btn_app_driver.clicked.connect(self.startcliked.emit)
        

        self.btn_terminal = QPushButton()
        self.btn_terminal.setIcon(icon_terminal)
        self.btn_terminal.setIconSize(ICON_SIZE)

        self.btn_calculator = QPushButton()
        self.btn_calculator.setIcon(icon_calc)
        self.btn_calculator.setIconSize(ICON_SIZE)

        self.btn_requests = QPushButton()
        self.btn_requests.setIcon(icon_requests)
        self.btn_requests.setIconSize(ICON_SIZE)

        self.btn_files = QPushButton()
        self.btn_files.setIcon(icon_file)
        self.btn_files.setIconSize(ICON_SIZE)


        self.lay_task_app.addWidget(self.space_left)
        self.lay_task_app.addWidget(self.btn_terminal)
        self.lay_task_app.addWidget(self.btn_requests)
        self.lay_task_app.addWidget(self.btn_app_driver)
        self.lay_task_app.addWidget(self.btn_calculator)
        self.lay_task_app.addWidget(self.btn_files)
        self.lay_task_app.addWidget(self.space_right)

# ================================================================== #
