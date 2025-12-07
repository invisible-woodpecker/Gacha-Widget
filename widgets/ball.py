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



class TraceWidget(QWidget):
    def __init__(self, parent_ball, position):
        super().__init__()

        self.parent_ball = parent_ball 
        
        self.setFixedSize(100, 50)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        path_ball_crashed = resource_path("assets/ball_crashed.png")
        self.pixmap = QPixmap(path_ball_crashed)
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        scaled_pixmap = self.pixmap.scaled(self.size(), 
                                             Qt.AspectRatioMode.KeepAspectRatio, 
                                             Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;")

        self.move(position)

        self.show()



class BallWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFixedSize(100, 150) 
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.is_dragging = False
        self.drag_start_position = QPoint()
        self.old_pos = None

        path_ball_normal = resource_path("assets/ball_normal.png")
        path_ball_up = resource_path("assets/ball_up.png")
        self.default_pixmap = QPixmap(path_ball_normal)
        self.up_pixmap = QPixmap(path_ball_up)

        self.traces = [] 

        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;") 
        
        self.update_image(self.default_pixmap)



    def update_image(self, pixmap):
        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatio, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        


    def closeEvent(self, event):
        for trace in list(self.traces): 
            if trace.isVisible():
                trace.close()
 
        self.traces.clear() 
        super().closeEvent(event)



    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.globalPosition().toPoint()
            self.old_pos = event.globalPosition().toPoint()
            self.is_dragging = False
            self.update_image(self.up_pixmap)
            event.accept()



    def mouseMoveEvent(self, event: QMouseEvent):
        if self.old_pos is not None and event.buttons() == Qt.MouseButton.LeftButton:
            distance = (event.globalPosition().toPoint() - self.drag_start_position).manhattanLength()
            if distance > 5:
                self.is_dragging = True

            if self.is_dragging:
                delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.old_pos = event.globalPosition().toPoint()
            event.accept()



    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.update_image(self.default_pixmap)

            trace_position = self.geometry().bottomLeft() 
            trace_position.setY(trace_position.y() - 50)
            
            self.create_trace(trace_position)

            self.old_pos = None
            self.is_dragging = False
            event.accept()



    def create_trace(self, position):
        trace = TraceWidget(self, position)

        self.traces.append(trace)
