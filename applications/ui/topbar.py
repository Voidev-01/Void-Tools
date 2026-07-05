# ========== Moduls ========== #
from datetime import *

import qtawesome as qta

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from utils.functions import close_window
# ================================================== #


# ========== class TopBar ========== #

class TopBar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("topbars")
        self.setFixedHeight(40)
        self.space_left = QWidget()
        self.space_left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.space_right = QWidget()
        self.space_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        ICON_SIZE = QSize(20,20)

        self.now = datetime.now().strftime("%H:%M")
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_set)
        self.timer.start(1000)

        self.layout_btn_bar = QHBoxLayout()
        self.setLayout(self.layout_btn_bar)
        
       
        icon_power = qta.icon("fa6s.power-off",color="white")
        icon_setting = qta.icon("ri.settings-5-fill",color="white")
        icon_reload = qta.icon("mdi6.reload",color="white")
        icon_notif = qta.icon("ri.notification-3-fill",color="white")
        self.btn_power = QPushButton()
        self.btn_power.setIcon(icon_power)
        self.btn_power.setIconSize(ICON_SIZE)
        self.btn_power.setObjectName("btn_power")
        self.btn_power.clicked.connect(close_window)
       
        self.btn_setting = QPushButton()
        self.btn_setting.setIcon(icon_setting)
        self.btn_setting.setIconSize(ICON_SIZE)

        self.btn_reload = QPushButton()
        self.btn_reload.setIcon(icon_reload)
        self.btn_reload.setIconSize(ICON_SIZE)

        self.btn_notif = QPushButton()
        self.btn_notif.setIcon(icon_notif)
        self.btn_notif.setIconSize(ICON_SIZE)
    
        

        self.btn_setting.setObjectName("btn_setting")
        self.clock = QLabel(self.now)
    
        self.clock.setObjectName("clock")    
        self.layout_btn_bar.addWidget(self.btn_power)
        self.layout_btn_bar.addWidget(self.btn_setting)
        self.layout_btn_bar.addWidget(self.space_left)
        self.layout_btn_bar.addWidget(self.clock)
        self.layout_btn_bar.addWidget(self.space_right)
        self.layout_btn_bar.addWidget(self.btn_reload)
        self.layout_btn_bar.addWidget(self.btn_notif)


    def time_set(self):
        now_time = datetime.now().strftime("%H:%M")
        self.clock.setText(now_time)


