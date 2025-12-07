from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QMouseEvent, QFont
from PyQt6.QtCore import Qt, QPoint, QTimer, QDateTime

class ClockWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFixedSize(150, 50)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        self.old_pos = None          
        self.is_dragging = False
        
        self.time_label = QLabel(self)
        self.time_label.setGeometry(0, 0, self.width(), self.height())
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font = QFont("Arial", 20, QFont.Weight.Bold)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("""
            color: black; 
            background-color: white; 
            border-radius: 10px;
        """)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()



    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)



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