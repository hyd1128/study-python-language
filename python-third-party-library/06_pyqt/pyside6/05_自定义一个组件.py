#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt


class GreenDotWidget(QWidget):
    def __init__(self, size=1, parent=None):
        super().__init__(parent)
        self.size = size  # 设定圆点大小
        self.setFixedSize(size, size)  # 设置组件固定大小

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        painter.setBrush(QColor(0, 255, 0))  # 绿色填充
        painter.setPen(Qt.NoPen)  # 无边框
        painter.drawEllipse(0, 0, self.size, self.size)  # 画圆


app = QApplication([])
dot = GreenDotWidget(size=20)  # 20px 绿色圆点
dot.show()
app.exec()
