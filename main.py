import sys
from PyQt6.QtWidgets import QApplication
from widgets.gacha_machine import MainGachaWidget 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_widget = MainGachaWidget()
    
    screen = QApplication.primaryScreen().geometry()
    
    x = (screen.width() - main_widget.width()) // 2
    y = (screen.height() - main_widget.height()) // 2
    
    main_widget.move(x, y)
    
    main_widget.show()
    sys.exit(app.exec())