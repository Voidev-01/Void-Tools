import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from ui.main_window import MainWindow
from ui.notification import NotificationDialog
from utils.qss import open_file_qss


apps = QApplication(sys.argv)

qss = open_file_qss("src/dark_theme_qss")
apps.setStyleSheet(qss)

window = MainWindow()

QTimer.singleShot(
    5000,
    lambda: NotificationDialog("For Exit Clicked Esc or power btn").exec()
)

window.showFullScreen()
sys.exit(apps.exec())