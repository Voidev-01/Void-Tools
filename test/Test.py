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
QLabel,QToolBar,QSizePolicy,QVBoxLayout,QHBoxLayout,QPushButton,QMessageBox,QDialog)
from PySide6.QtCore import Qt,QTimer,QSize
from PySide6.QtGui import QAction,QPixmap,QPainter,QIcon,QShortcut,QKeySequence
import qtawesome as qta
import requests
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
        shortcut_esc = QShortcut(QKeySequence(Qt.Key_Escape), self)
        shortcut_esc.activated.connect(close_window)
        
        
        

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


class Desktop(QWidget):
    def __init__(self):
        super().__init__()
        
        ICON_SIZE = QSize(50,50)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.original_wallpaper = QPixmap("/home/mahdi/Void-tools/assets/image/bbbbbbb.png")
        self.scaled_wallpaper = None
        self.update_wallpaper()
        self.setObjectName("desktops")
        self.layout_app = QVBoxLayout()
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

        painter.drawPixmap(self.rect(), self.scaled_wallpaper)



class TaskBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.space_left = QWidget()
        self.space_left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.space_right = QWidget()
        self.space_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        ICON_SIZE = QSize(32,32)
        self.setObjectName("taskbars")
        self.setFixedHeight(45)
        self.lay_task_app = QHBoxLayout()
        self.setLayout(self.lay_task_app)

       

        icon_terminal = qta.icon("ph.terminal-window-fill",color="white")
        icon_calc = qta.icon("ph.calculator-fill",color="white")
        icon_requests = qta.icon("fa5s.eye",color="white")
        icon_file = qta.icon("msc.file-directory",color="white")

        self.btn_app_driver = QPushButton()
        self.btn_app_driver.setIcon(QIcon("/home/mahdi/Void-tools/assets/icons/icon_3232.png"))
        ICON_SIZE_DRI = QSize(100,90)
        self.btn_app_driver.setIconSize(ICON_SIZE_DRI)
        

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

class NotificationDialog(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("info")
        self.setFixedSize(400, 200)
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setWordWrap(True)
        btn = QPushButton("ok")
        btn.clicked.connect(self.accept)
        layout.addWidget(label)
        layout.addWidget(btn)
        self.setLayout(layout)

        

def close_window():
    QApplication.instance().quit()


# ========== For_run_app ========== #
app = QApplication()
get_file_name = open_file_qss("/home/mahdi/Void-tools/src/dark_theme_qss")

app.setStyleSheet(get_file_name)
window = MainWindow()
QTimer.singleShot(5000, lambda: NotificationDialog("For Exit Cliked Esc").exec())
window.showFullScreen()
sys.exit(app.exec())
