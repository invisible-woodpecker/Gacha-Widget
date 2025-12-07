# <Gacha-Widget> - Gacha Machine Desktop App
# Copyright (C) <2025> <Hyeongyu Hwang>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

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
