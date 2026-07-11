from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import qtawesome as qta

from utils.functions import close_window

ICON_SIZE = QSize(48, 48)


class StartMenu(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setFixedSize(700, 500)

        self.setStyleSheet("""
        QWidget{
            background: rgba(25,25,25,180);
            border:1px solid rgba(255,255,255,35);
            border-radius:20px;
        }

        QLineEdit{
            background: rgba(40,40,40,180);
            color:white;
            border:none;
            border-radius:12px;
            padding:10px;
            font-size:15px;
        }

        QPushButton{
            background:transparent;
            border:none;
            color:white;
            border-radius:14px;
            padding:10px;
        }

        QPushButton:hover{
            background:rgba(255,255,255,19);
        }

        QLabel{
            color:white;
        }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20,20,20,20)
        main_layout.setSpacing(18)

        # ---------------- Search ----------------

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        main_layout.addWidget(self.search)

        # ---------------- Apps ----------------

        grid = QGridLayout()
        grid.setSpacing(12)

        apps = [
            ("mdi6.google-chrome", "Chrome"),
            ("mdi6.google-translate", "Translate"),
            ("msc.github-inverted", "Github"),
            ("msc.game", "Games"),
            ("mdi.gmail", "Gmail"),
            ("ph.chat-teardrop-dots-light", "Chat"),
            ("fa5.user-circle", "Profile"),
            ("fa5b.amazon", "Amazon"),
            ("ph.note-pencil", "Notes"),
            ("fa5b.spotify", "Spotify"),
            ("ph.terminal-window-fill", "Terminal"),
            ("ph.folder-fill", "Files"),
        ]

        row = 0
        col = 0

        for icon_name, text in apps:

            button = QToolButton()

            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            button.setIcon(qta.icon(icon_name, color="white"))

            button.setIconSize(ICON_SIZE)

            button.setText(text)
            

            button.setFixedSize(110,100)

            grid.addWidget(button, row, col)

            col += 1

            if col == 4:
                col = 0
                row += 1

        main_layout.addLayout(grid)

        main_layout.addStretch()

        # ---------------- Bottom ----------------

        bottom = QHBoxLayout()

        

        #bottom.addWidget(self.user)

        bottom.addStretch()

        self.setting = QPushButton()

        self.setting.setIcon(qta.icon("ri.settings-5-fill", color="#afafaf"))

        self.setting.setIconSize(QSize(28,28))

        bottom.addWidget(self.setting)

        self.power = QPushButton()

        self.power.setIcon(qta.icon("fa6s.power-off", color="#afafaf"))

        self.power.setIconSize(QSize(28,28))
        self.power.clicked.connect(close_window)

        bottom.addWidget(self.power)

        main_layout.addLayout(bottom)

        # ---------------- Animation ----------------

        self.hide()

        self.show_animation = QPropertyAnimation(self, b"geometry")
        self.show_animation.setDuration(250)
        self.show_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.hide_animation = QPropertyAnimation(self, b"geometry")
        self.hide_animation.setDuration(250)
        self.hide_animation.setEasingCurve(QEasingCurve.InCubic)
        self.hide_animation.finished.connect(self.hide)

    def show_menu(self):

        parent = self.parent()

        end_x = (parent.width() - self.width()) // 2
        end_y = (parent.height() - self.height()) // 2

        start_rect = QRect(
            end_x,
            parent.height(),
            self.width(),
            self.height()
        )

        end_rect = QRect(
            end_x,
            end_y,
            self.width(),
            self.height()
        )

        self.setGeometry(start_rect)
        self.show()
        self.raise_()

        self.show_animation.stop()
        self.show_animation.setStartValue(start_rect)
        self.show_animation.setEndValue(end_rect)
        self.show_animation.start()

    def hide_menu(self):

        parent = self.parent()

        start_rect = self.geometry()

        end_rect = QRect(
            start_rect.x(),
            parent.height(),
            self.width(),
            self.height()
        )

        self.hide_animation.stop()
        self.hide_animation.setStartValue(start_rect)
        self.hide_animation.setEndValue(end_rect)
        self.hide_animation.start()