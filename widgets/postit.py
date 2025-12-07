from PyQt6.QtWidgets import QWidget, QTextEdit, QLabel 
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



class PostItWidget(QWidget):
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

        path_postit = resource_path("assets/postit.png")
        pixmap = QPixmap(path_postit)
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatio, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;") 

        self.text_editor = TextEditableAndDraggable(self)
        self.text_editor.setGeometry(5, 5, self.width() - 10, self.height() - 10) 
        self.text_editor.setStyleSheet("""
            color: black;
            background-color: transparent;
            font-size: 10px;
            border: none;
        """)
        self.text_editor.setPlaceholderText("~~^-^~~...")
        
        self.text_editor.parent_widget = self



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



class TextEditableAndDraggable(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent) 
        
        self.parent_widget = None
        self.old_pos = None
        self.is_dragging = False



    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.parent_widget:
                self.parent_widget.old_pos = event.globalPosition().toPoint()
                self.parent_widget.is_dragging = True
                
            self.setFocus()
        
        super().mousePressEvent(event)
        event.accept()
        
        
        
    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            if self.parent_widget and self.parent_widget.is_dragging:
                delta = QPoint(event.globalPosition().toPoint() - self.parent_widget.old_pos)
                self.parent_widget.move(self.parent_widget.x() + delta.x(), self.parent_widget.y() + delta.y())
                self.parent_widget.old_pos = event.globalPosition().toPoint()
                event.accept()
                return

        super().mouseMoveEvent(event)



    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.parent_widget:
            self.parent_widget.old_pos = None
            self.parent_widget.is_dragging = False
            
        super().mouseReleaseEvent(event)
        event.accept()