#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/1 11:01
# @Author : limber
# @desc :
import sys

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)
        self.btn1 = QPushButton('计数')
        self.btn2 = QPushButton('停止')
        self.btn1.clicked.connect(self.start_counting)
        self.btn2.clicked.connect(self.stop_counting)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000000)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.spin_box)
        v_layout.addWidget(self.btn1)
        v_layout.addWidget(self.btn2)
        self.setLayout(v_layout)

        self.count_thread = CountThread(self)  # 1
        self.count_thread.count_signal.connect(self.update_label)

    def start_counting(self):
        if not self.count_thread.isRunning():
            self.count_thread.start()

    def stop_counting(self):
        self.count_thread.stop()

    def update_label(self, num):
        self.label.setText(str(num))


class CountThread(QThread):
    count_signal = pyqtSignal(int)

    def __init__(self, window):  # 注释1开始
        super(CountThread, self).__init__()
        self.flag = True
        self.window = window

    def run(self):
        num = self.window.spin_box.value()  # 注释1结束
        self.flag = True

        while num < 10000000:
            if not self.flag:
                break

            num += 1
            self.count_signal.emit(num)
            self.msleep(100)

    def stop(self):
        # self.flag = False
        self.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
