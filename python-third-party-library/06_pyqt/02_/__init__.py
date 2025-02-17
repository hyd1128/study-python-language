#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/11/1 14:34
# @Author : limber
# @desc :


from PyQt6 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建中心部件
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)

        # 创建水平布局
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)

        # 创建 QLabel
        self.label = QtWidgets.QLabel("prism", self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)  # 设置字体大小
        self.label.setFont(font)

        # 添加 QLabel 到布局
        self.horizontalLayout_3.addWidget(self.label)

# 创建应用和主窗口
app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
