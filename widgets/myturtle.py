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
from PyQt6.QtCore import Qt, QPoint, QTimer

import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class TurtleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFixedSize(125, 125)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.is_dead = False
        self.is_hungry = False

        self.is_dragging = False
        self.old_pos = None

        path_turtle_normal = resource_path("assets/myturtle_normal.png")
        path_turtle_hungry = resource_path("assets/myturtle_hungry.png")
        path_turtle_killed = resource_path("assets/myturtle_killed.png")
        self.normal_pixmap = QPixmap(path_turtle_normal)
        self.hungry_pixmap = QPixmap(path_turtle_hungry)
        self.killed_pixmap = QPixmap(path_turtle_killed)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;") 
        
        self.update_image()
        
        self.hunger_timer = QTimer(self)
        self.hunger_timer.timeout.connect(self.become_hungry)
        self.reset_hunger_timer()



    def update_image(self):
        if self.is_dead:
            pixmap = self.killed_pixmap
        elif self.is_hungry:
            pixmap = self.hungry_pixmap
        else:
            pixmap = self.normal_pixmap

        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatio, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)



    def become_hungry(self):
        if not self.is_dead:
            self.is_hungry = True
            self.update_image()



    def reset_hunger_timer(self):
        if self.is_dead:
            return
            
        self.is_hungry = False
        self.update_image()
        self.hunger_timer.stop()
        self.hunger_timer.start(5000)



    def kill(self):
        self.is_dead = True
        self.is_dragging = False
        self.hunger_timer.stop()
        self.update_image()



    def mousePressEvent(self, event: QMouseEvent):
        if self.is_dead:
            event.ignore()
            return
            
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            self.is_dragging = True
            event.accept()



    def mouseMoveEvent(self, event: QMouseEvent):
        if self.is_dead:
            event.ignore()
            return

        if self.old_pos is not None and event.buttons() == Qt.MouseButton.LeftButton and self.is_dragging:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()
            event.accept()



    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.is_dead:
            event.ignore()
            return

        self.old_pos = None
        self.is_dragging = False

        event.accept()
