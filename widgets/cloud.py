from PyQt6.QtWidgets import QWidget, QLabel, QApplication
from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtCore import Qt, QTimer
import random

import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class CloudWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFixedSize(132, 80)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.is_dragging = False
        
        self.move_speed_x = 7.0
        self.move_speed_y = 1.5 
        
        path_cloud = resource_path("assets/cloud.png")
        pixmap = QPixmap(path_cloud) 
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;") 

        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.auto_move)
        self.move_timer.start(10) 

        self.random_timer = QTimer(self)
        self.random_timer.timeout.connect(self.randomize_movement)
        self.random_timer.start(200)



    def randomize_movement(self):
        self.move_speed_x = random.uniform(-10.0, 10.0)
        self.move_speed_y = random.uniform(-10.0, 10.0)



    def auto_move(self):
        current_x = self.x()
        current_y = self.y()
        
        app_instance = QApplication.instance()
        if not app_instance: 
            return

        screen_geometry = app_instance.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        new_x = current_x + self.move_speed_x
        new_y = current_y + self.move_speed_y

        if new_x > screen_width:
            new_x = -self.width() 
        elif new_x < -self.width():
             new_x = screen_width 

        if new_y > screen_height:
            new_y = -self.height() 
        elif new_y < -self.height():
             new_y = screen_height 
            
        self.move(int(new_x), int(new_y))



    def mousePressEvent(self, event: QMouseEvent):
        event.ignore()



    def mouseMoveEvent(self, event: QMouseEvent):
        event.ignore()



    def mouseReleaseEvent(self, event: QMouseEvent):
        event.ignore()