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

from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QSizePolicy
from PyQt6.QtGui import QMouseEvent, QPixmap, QFont
from PyQt6.QtCore import Qt, QPoint, QRect
import random

import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class CookieWidget(QWidget):
    ADJECTIVES = [
        "뜻밖의",
        "신비로운",    "거대한",    "미세한",     "빠른",      "느린",
        "부드러운",    "거친",      "차가운",     "따뜻한",    "밝은",
        "어두운",      "조용한",    "시끄러운",   "새로운",    "오래된",
        "강한",        "약한",      "예쁜",      "못생긴",    "똑똑한",
        "멍청한",      "고요한",    "활기찬",     "단단한",    "무른",
        "날카로운",    "둥근",      "평평한",     "짧은",      "긴",
        "깊은",        "얕은",      "넓은",      "좁은",      "무거운",
        "가벼운",      "충실한",    "불완전한",   "순수한",     "혼란스러운",
        "매운",        "달콤한",    "쓸모없는",   "쓴",        "담백한",
        "화려한",      "단순한",    "복잡한",     "기쁜",      "슬픈",
        "지친",        "피곤한",    "희미한",     "선명한",    "창의적인",
        "평범한",      "독특한",    "고급스러운", "오래가는",   "순간적인",
        "날렵한",      "투명한",    "불투명한",   "축축한",     "건조한",
        "기묘한",      "자연스러운","인공적인",    "진한",      "연한",
        "공허한",      "가득한",    "친절한",     "무례한",     "담대한",
        "소심한",      "화난",      "온화한",     "굳건한",    "부주의한",
        "신중한",      "균형잡힌",  "왜곡된",     "깨끗한",     "더러운",
        "느긋한",      "급한",      "완벽한",     "불안한",    "명확한",
        "애매한",      "무심한",    "열정적인",   "냉정한",     "활발한",
        "정적인",      "모험적인",  "소소한",     "화사한",     "칙칙한",
    ]
    NOUNS = [
        "행운",
        "사랑", "희망", "용기", "자유", "평화", "행복", "슬픔", "기쁨", "분노", "삶",
        "신뢰", "배려", "존중", "인내", "의지", "결심", "목표", "믿음", "추억", "분석",
        "지혜", "지식", "경험", "감정", "욕망", "열정", "본능", "성취", "실패", "성공",
        "기회", "변화", "미래", "과거", "시간", "순간", "균형", "혼란", "안정", "혼돈",
        "정의", "공정", "권리", "의무", "책임", "도덕", "규칙", "질서", "신념", "가치",
        "의미", "목적", "영향", "선택", "판단", "결론", "지향", "의문", "이해", "두려움",
        "평온", "고독", "용서", "화해", "집중", "각성", "긴장", "여유", "안도", "창의성",
        "의심", "확신", "동기", "본질", "성향", "성격", "매력", "열망", "위기", "가능성",
        "패배", "승리", "희생", "공헌", "노력", "열의", "통찰", "직관", "성찰", "상상력",
        "질투", "욕심", "충동", "감사", "감탄", "집착", "애정", "여정", "상상", "자존감" 
    ]



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
        self.is_opened = False
        
        self.drag_start_position = QPoint()
        
        path_closed = resource_path("assets/cookie_closed.png")
        path_opened = resource_path("assets/cookie_opened.png")
        self.closed_pixmap = QPixmap(path_closed)
        self.opened_pixmap = QPixmap(path_opened)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: transparent;") 
        
        self.adjective_label = QLabel(self)
        self.adjective_label.setGeometry(10, 10, self.width() - 20, self.height() - 20)
        self.adjective_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adjective_label.setStyleSheet("""
            color: black;
            font-weight: bold;
            font-size: 20px;
            background-color: transparent;
        """)
        self.adjective_label.hide()
        
        self.noun_label = QLabel(self)
        self.noun_label.setGeometry(10, 10, self.width() - 20, self.height() - 20)
        self.noun_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.noun_label.setStyleSheet("""
            color: black;
            font-weight: bold;
            font-size: 20px;
            background-color: transparent;
        """)
        self.noun_label.hide()
        
        self.update_cookie_image()



    def update_cookie_image(self):
        if self.is_opened:
            pixmap = self.opened_pixmap         
            self.setFixedSize(400, 100)
        
        else:
            pixmap = self.closed_pixmap
            self.setFixedSize(100, 100) 

        self.image_label.setGeometry(0, 0, self.width(), self.height())
        scaled_pixmap = pixmap.scaled(self.size(), 
                                      Qt.AspectRatioMode.KeepAspectRatio, 
                                      Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)

        if self.is_opened:

            ADJ_X = 55
            ADJ_Y = -15
            ADJ_WIDTH = 160
            ADJ_HEIGHT = 70

            NOUN_X = 200
            NOUN_Y = 0
            NOUN_WIDTH = 160
            NOUN_HEIGHT = 70
            
            self.adjective_label.setGeometry(ADJ_X, ADJ_Y, ADJ_WIDTH, ADJ_HEIGHT)
            self.noun_label.setGeometry(NOUN_X, NOUN_Y, NOUN_WIDTH, NOUN_HEIGHT)
            
        else:
            text_margin = 10 
            temp_rect = QRect(text_margin, text_margin, 
                              self.width() - 2 * text_margin, 
                              self.height() - 2 * text_margin)
            self.adjective_label.setGeometry(temp_rect)
            self.noun_label.setGeometry(temp_rect)



    def open_cookie(self):
        if self.is_opened:
            return

        adjective = random.choice(self.ADJECTIVES)
        noun = random.choice(self.NOUNS)
        
        self.adjective_label.setText(adjective)
        self.noun_label.setText(noun)
        
        self.is_opened = True
        
        self.update_cookie_image()
        
        self.adjective_label.show()
        self.noun_label.show()



    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.globalPosition().toPoint()
            self.old_pos = event.globalPosition().toPoint()
            self.is_dragging = False
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
            if not self.is_dragging:
                self.open_cookie()
            
            self.old_pos = None
            self.is_dragging = False

            event.accept()
