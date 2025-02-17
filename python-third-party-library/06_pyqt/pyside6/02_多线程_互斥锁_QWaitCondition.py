#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import sys
from PySide6.QtCore import (QThread, QWaitCondition, QMutex, Signal, QMutexLocker)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QProgressBar, QApplication)


class MyThread(QThread):
    valueChange = Signal(int)

    def __init__(self):
        super().__init__()
        self.is_paused = bool()
        self.progress_value = int(0)
        self.mutex = QMutex()
        self.cond = QWaitCondition()

    def pause_thread(self):
        with QMutexLocker(self.mutex):
            self.is_paused = True

    def resume_thread(self):
        if not self.is_paused:
            return
        with QMutexLocker(self.mutex):
            self.is_paused = False
            # 释放其它线程
            self.cond.wakeOne()

    def run(self):
        while True:
            with QMutexLocker(self.mutex):
                while self.is_paused:
                    # 阻塞当前线程
                    self.cond.wait(self.mutex)
                if self.progress_value > 100:
                    self.progress_value = 0
                    return
                self.progress_value += 1
                self.valueChange.emit(self.progress_value)
                self.msleep(10)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_thread()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)
        layout.addWidget(QPushButton(r'启动&&停止', self, clicked=self.paused_thread))
        layout.addWidget(QPushButton('恢复线程', self, clicked=self.wake_thread))
        self.show()

    def setup_thread(self):
        self.thread = MyThread()
        self.thread.valueChange.connect(self.progressBar.setValue)

    def paused_thread(self):
        if not self.thread.isRunning():
            self.thread.start()
        else:
            self.thread.pause_thread()

    def wake_thread(self):
        self.thread.resume_thread()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())
