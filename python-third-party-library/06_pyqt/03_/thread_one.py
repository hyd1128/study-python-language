#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/1 17:43
# @Author : limber
# @desc :
from PyQt6 import QtCore
from PyQt6.QtCore import QThread


class ThreadOne(QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.flag = True

    def run(self):
        num = 0

        while num < 1000000:
            if not self.flag:
                break

            msg = f"当前信息是第 {num + 1} 条"
            num += 1
            print(msg)
            # 发射信号
            self.signal.emit(msg)
            self.msleep(100)

    def stop(self):
        self.flag = False
