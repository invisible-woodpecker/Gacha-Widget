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
