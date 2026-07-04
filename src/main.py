"""
Copyright (c) 2026 Voidev

This file is part of Void-Tools.

Licensed under the Void-Tools Source-Available License (VTSAL).
See the LICENSE file for details.
"""
# ============================================================================================= #
# ========== call_Moduls========== #
from datetime import *
import sys
from PySide6.QtWidgets import (QApplication,QMainWindow,QWidget,
QLabel,QToolBar,QSizePolicy,QVBoxLayout,QHBoxLayout,QPushButton)
from PySide6.QtCore import Qt,QTimer,QSize
from PySide6.QtGui import QAction,QPixmap,QPainter
import qtawesome as qta

# ====================================================== #
#def open_file_theme(file_name:str):
    #with open(file_name,'r') as f:
        #return f.read()
def open_file_qss(file_name:str):
    with open(file_name,'r',encoding='utf-8') as f:
        return f.read()

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

        self.now = datetime.now().strftime("|%d| %H:%M")
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_set)
        self.timer.start(1000)

        self.layout_btn_bar = QHBoxLayout()
        self.setLayout(self.layout_btn_bar)
        
       
        icon_power = qta.icon("fa6s.power-off",color="white")
        self.btn_power = QPushButton()
        self.btn_power.setIcon(icon_power)
        self.btn_power.setIconSize(ICON_SIZE)
        self.btn_power.setObjectName("btn_power")
        self.btn_power.clicked.connect(close_window)
        icon_setting = qta.icon("ri.settings-5-fill",color="white")
        self.btn_setting = QPushButton()
        self.btn_setting.setIcon(icon_setting)
        self.btn_setting.setIconSize(ICON_SIZE)

        self.btn_setting.setObjectName("btn_setting")
        self.clock = QLabel(self.now)
    
        self.clock.setObjectName("clock")    
        self.layout_btn_bar.addWidget(self.btn_power)
        self.layout_btn_bar.addWidget(self.btn_setting)
        self.layout_btn_bar.addWidget(self.space_left)
        self.layout_btn_bar.addWidget(self.clock)
        self.layout_btn_bar.addWidget(self.space_right)

    def time_set(self):
        now_time = datetime.now().strftime("|%d| %H:%M")
        self.clock.setText(now_time)


class Desktop(QWidget):
    def __init__(self):
        super().__init__()
        
        ICON_SIZE = QSize(35,35)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.original_wallpaper = QPixmap("/home/mahdi/Void-tools/assets/image/backg.png")
        self.scaled_wallpaper = None
        self.update_wallpaper()
        self.setObjectName("desktops")
        self.layout_app = QHBoxLayout()
        self.setLayout(self.layout_app)
        
    def load_wallpaper(self):
        pass

    def update_wallpaper(self):
        if self.original_wallpaper.isNull():
            return

        self.scaled_wallpaper = self.original_wallpaper.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
    )

    def resizeEvent(self,event):
        self.update_wallpaper()
        super().resizeEvent(event)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.scaled_wallpaper is None:
            return
        
        painter = QPainter(self)

        #x = (self.width() - self.scaled_wallpaper.width()) // 2
        #y = (self.height() - self.scaled_wallpaper.height()) // 2

        #painter.drawPixmap(x, y, self.scaled_wallpaper)
        painter.drawPixmap(self.rect(), self.scaled_wallpaper)



class TaskBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.space_left = QWidget()
        self.space_left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.space_right = QWidget()
        self.space_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        ICON_SIZE = QSize(30,30)
        self.setObjectName("taskbars")
        self.setFixedHeight(45)
        self.lay_task_app = QHBoxLayout()
        self.setLayout(self.lay_task_app)
        icon_app_drive = qta.icon("ri.apps-2-line",color="white")
        self.btn_app_driver = QPushButton()
        self.btn_app_driver.setIcon(icon_app_drive)
        self.btn_app_driver.setIconSize(ICON_SIZE)

        self.lay_task_app.addWidget(self.space_left)
        #
        self.lay_task_app.addWidget(self.btn_app_driver)
        #
        self.lay_task_app.addWidget(self.space_right)

        

def close_window():
    window.close()


# ========== For_run_app ========== #
app = QApplication()
get_file_name = open_file_qss("/home/mahdi/Void-tools/src/dark_theme_qss")

app.setStyleSheet(get_file_name)
window = MainWindow()
window.showFullScreen()
sys.exit(app.exec())
