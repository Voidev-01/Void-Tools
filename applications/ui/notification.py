# ============ Moduls =============== #
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
# ==================================== #


# ========== class Notification =============== #
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


# =================================================== #
