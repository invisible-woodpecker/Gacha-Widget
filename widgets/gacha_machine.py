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

import random

from PyQt6.QtWidgets import (
    QWidget, QLabel, QApplication,
    QMenu
)
from PyQt6.QtGui import QMouseEvent, QAction, QPixmap, QIcon
from PyQt6.QtCore import Qt, QPoint, QTimer

import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



from widgets.asparagus import AsparagusWidget
from widgets.blackhole import BlackHoleWidget
from widgets.postit import PostItWidget
from widgets.clock import ClockWidget
from widgets.cloud import CloudWidget
from widgets.cookie import CookieWidget
from widgets.ball import BallWidget
from widgets.myturtle import TurtleWidget

class MainGachaWidget(QWidget):
    ITEM_CLASSES = [AsparagusWidget, BlackHoleWidget, PostItWidget, ClockWidget, CloudWidget, CookieWidget, BallWidget, TurtleWidget] 

    def __init__(self, parent=None):
        super().__init__(parent) 
        self.setFixedSize(150, 150) 
        self.setWindowTitle("Gacha Machine")
        path_icon = resource_path("assets/gacha_machine.ico")
        self.setWindowIcon(QIcon(path_icon))
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint
        ) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        self.spawned_widgets = [] 
        
        self.old_pos = None
        self.is_dragging = False 
        self.drag_start_position = QPoint() 
        self.DRAG_THRESHOLD = 5
        
        self.collision_timer = QTimer(self)
        self.collision_timer.timeout.connect(self.check_for_deletion)
        self.collision_timer.start(50) 
        
        self.gacha_label = QLabel(self)
        self.gacha_label.setGeometry(0, 0, self.width(), self.height())
        
        path_gacha_machine = resource_path("assets/gacha_machine.png")
        pixmap = QPixmap(path_gacha_machine)
        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatio, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.gacha_label.setPixmap(scaled_pixmap)
        self.gacha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gacha_label.setStyleSheet("background-color: transparent;") 



    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            self.drag_start_position = event.position().toPoint() 
            self.is_dragging = False
            event.accept()



    def mouseMoveEvent(self, event: QMouseEvent):
        if self.old_pos is not None and event.buttons() == Qt.MouseButton.LeftButton:
            distance = (event.position().toPoint() - self.drag_start_position).manhattanLength()
            if distance > self.DRAG_THRESHOLD:
                self.is_dragging = True

            if self.is_dragging:
                delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.old_pos = event.globalPosition().toPoint() 
            event.accept()



    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if not self.is_dragging:
                self.spawn_widget() 

            self.old_pos = None
            self.is_dragging = False
            event.accept()



    def check_for_deletion(self):
        current_widgets = list(self.spawned_widgets) 
        
        item_widgets = [w for w in current_widgets
                         if isinstance(w, AsparagusWidget) or 
                            isinstance(w, PostItWidget) or
                            isinstance(w, ClockWidget) or
                            isinstance(w, CloudWidget) or 
                            isinstance(w, CookieWidget) or 
                            isinstance(w, BallWidget)
                        ]
        black_hole_widgets = [w for w in current_widgets
                              if isinstance(w, BlackHoleWidget)]
        turtle_widgets = [w for w in current_widgets
                           if isinstance(w, TurtleWidget)]
                           
        widgets_to_delete = []

        for turtle in turtle_widgets:
            if turtle.is_dead:
                continue

            if turtle.is_hungry:
                for asparagus in [w for w in current_widgets if isinstance(w, AsparagusWidget)]:
                    asparagus_center_point = asparagus.geometry().center()
                    if turtle.geometry().contains(asparagus_center_point):
                        widgets_to_delete.append(asparagus)
                        turtle.reset_hunger_timer()
                        break 
        
            for ball in [w for w in current_widgets if isinstance(w, BallWidget)]:
                ball_center_point = ball.geometry().center()
                if turtle.geometry().contains(ball_center_point):
                    widgets_to_delete.append(ball)
                    turtle.kill()
                    break

        all_deletable_items_by_hole = item_widgets + turtle_widgets

        for item in all_deletable_items_by_hole:
            for black_hole in black_hole_widgets: 
                hole_area = black_hole.geometry()
                item_area = item.geometry()

                if hole_area.intersects(item_area):
                    widgets_to_delete.append(item)
                    break 
        
        for dragged_hole in black_hole_widgets:
            if not dragged_hole.is_dragging:
                continue

            for stationary_hole in black_hole_widgets:
                if dragged_hole is stationary_hole:
                    continue
                
                dragged_hole_area = dragged_hole.geometry()
                stationary_hole_center = stationary_hole.geometry().center()

                if dragged_hole_area.contains(stationary_hole_center):
                    widgets_to_delete.append(stationary_hole)
                    break 
        
        for widget_instance in set(widgets_to_delete):
            if widget_instance in self.spawned_widgets:
                widget_instance.close()
                self.spawned_widgets.remove(widget_instance)



    def spawn_widget(self):
        WidgetClass = random.choice(self.ITEM_CLASSES)
        
        new_widget = WidgetClass()

        self.spawned_widgets.append(new_widget) 
        
        app_instance = QApplication.instance()
        if not app_instance: return

        screen = app_instance.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        base_x = self.x()
        base_y = self.y()

        spawn_x = random.randint(base_x - 100, base_x + 100)
        spawn_y = random.randint(base_y - 100, base_y + 100)
        
        max_x = screen_width - new_widget.width()
        max_y = screen_height - new_widget.height()
        final_x = max(0, min(spawn_x, max_x))
        final_y = max(0, min(spawn_y, max_y))

        new_widget.move(final_x, final_y)
        new_widget.show()



    def contextMenuEvent(self, event):
        menu = QMenu(self)

        reset_action = QAction("초기화", self)
        reset_action.triggered.connect(self.reset_gacha)
        menu.addAction(reset_action)
        menu.addSeparator()
        
        exit_action = QAction("종료", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        menu.addAction(exit_action)
        menu.exec(event.globalPos())



    def reset_gacha(self):
        for widget in self.spawned_widgets:
            widget.close() 

        self.spawned_widgets.clear()
