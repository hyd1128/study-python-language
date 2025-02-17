#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/1 11:01
# @Author : limber
# @desc :
import sys

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)
        self.btn = QPushButton('计数')
        self.btn.clicked.connect(self.count)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)
        self.count_thread = CountThread()  # 注释1开始
        self.count_thread.count_signal.connect(self.update_label)

    def count(self):
        self.count_thread.start()

    def update_label(self, num):
        self.label.setText(str(num))  # 注释1结束


class CountThread(QThread):  # 注释2开始
    count_signal = pyqtSignal(int)

    def __init__(self):
        super(CountThread, self).__init__()

    def run(self):
        num = 0
        while num < 10000000:
            num += 1
            self.count_signal.emit(num)  # 注释2结束


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
