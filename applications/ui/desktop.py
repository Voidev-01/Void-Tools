# ========== Moduls ========== #
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
# ================================================= # 

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

# ================================================ #

