#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
from PySide6.QtCore import (QThread, Signal, Qt)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)


class Worker(QThread):
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        print("Thread started")
        for i in range(2):
            print(f"Thread running {i}")
            self.msleep(1000)
        print("Thread finished")
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.thread = None

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.label = QLabel("Ready", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Start Thread", self)
        self.button.clicked.connect(self.start_thread)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.show()

    def start_thread(self):
        if not self.thread or not self.thread.isRunning():
            self.thread = Worker()
            self.thread.finished.connect(self.thread_finished)
            self.thread.start()
            self.label.setText("Running")
            self.thread.wait()

    def thread_finished(self):
        self.label.setText("Finished")
        self.thread.deleteLater()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())

"""
创建线程对象：代码中通过创建 Worker 类来继承 QThread 类，并在 Worker 类中重写 run() 方法实现多线程执行的逻辑；
启动线程：在主窗口类 MainWindow 中的 start_thread() 方法中，通过创建 Worker 类的实例并调用 start() 方法来启动新的线程；
运行线程：在 run() 方法中，通过使用 msleep() 方法来模拟耗时操作；
线程等待：在start_thread()方法中使用了 self.thread.wait()阻塞当前线程；
结束线程：在 Worker 类的 run() 方法中，当完成耗时操作后，会发送一个 finished 信号，然后线程结束。主窗口类中，可以通过 finished 信号的连接函数 thread_finished() 来在线程结束时进行一些处理；
销毁线程对象：在 thread_finished() 方法中，通过调用 deleteLater() 方法来销毁线程对象，从而保证了线程对象的正确释放。
"""
