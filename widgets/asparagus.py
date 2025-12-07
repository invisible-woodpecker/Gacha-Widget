from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtCore import Qt, QPoint

import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class AsparagusWidget(QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        
        self.setFixedSize(100, 100)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
                
        self.is_dragging = False
        self.old_pos = None  

        path_asparagus = resource_path("assets/asparagus.png")
        pixmap = QPixmap(path_asparagus)        
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())     
        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatio, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;")



    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            self.is_dragging = True
            event.accept()



    def mouseMoveEvent(self, event: QMouseEvent):
        if self.old_pos is not None and event.buttons() == Qt.MouseButton.LeftButton and self.is_dragging:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()
            event.accept()



    def mouseReleaseEvent(self, event: QMouseEvent):
        self.old_pos = None
        self.is_dragging = False
        event.accept()