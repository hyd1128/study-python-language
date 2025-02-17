#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys

from PySide6.QtCore import QMutex, QThread, Signal, Slot, QMutexLocker
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout,
                               QWidget)


class Worker(QThread):
    valueChanged = Signal(tuple)

    def __init__(self, name, mutex, main_window):
        super().__init__()
        self.name = name
        # 创建互斥锁
        self.mutex = mutex
        self.main_window = main_window

    def run(self):
        for i in range(5):
            # 不需要手动解锁，QMutexLocker会在离开作用域时自动解锁
            with QMutexLocker(self.mutex):
                self.main_window.count += 1
                self.msleep(100)
                self.valueChanged.emit((self.name, self.main_window.count))


class MainWindow(QWidget):
    def __init__(self):
        self.count = int()
        self.mutex = QMutex()  # 定义锁对象
        super().__init__()
        self.setup_ui()
        self.setup_thread()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Count: 0", self)

        self.btn_start = QPushButton("Start", self)
        self.btn_start.clicked.connect(self.start_threads)

        layout.addWidget(self.label)
        layout.addWidget(self.btn_start)
        self.setLayout(layout)
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def setup_thread(self):
        self.worker1 = Worker('thread_1', self.mutex, self)
        self.worker2 = Worker('thread_2', self.mutex, self)
        self.worker1.valueChanged.connect(self.thread_finished)
        self.worker2.valueChanged.connect(self.thread_finished)

    def start_threads(self):
        self.worker1.start()
        self.worker2.start()

    @Slot(tuple)
    def thread_finished(self, value):
        print(str(value))
        self.label.setText(f"{str(value)}")


if __name__ == '__main__':
    app = QApplication()
    ex = MainWindow()
    sys.exit(app.exec())
