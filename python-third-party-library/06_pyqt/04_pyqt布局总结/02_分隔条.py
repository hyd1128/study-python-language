#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSplitter, QTextEdit, QListWidget, QVBoxLayout
from PyQt6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建 QSplitter
        # 水平分隔器
        # splitter = QSplitter(Qt.Orientation.Horizontal)
        # 垂直分隔器
        splitter = QSplitter(Qt.Orientation.Vertical)

        # 创建 QTextEdit 和 QListWidget
        text_edit = QTextEdit("这是一个文本编辑框")
        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

        # 将两个控件添加到 QSplitter 中
        splitter.addWidget(text_edit)
        splitter.addWidget(list_widget)

        # 设置 QSplitter 的初始大小
        splitter.setSizes([300, 200])

        # 创建布局并将 QSplitter 添加到其中
        layout = QVBoxLayout()
        layout.addWidget(splitter)

        # 设置窗口的布局
        self.setLayout(layout)

        # 设置窗口标题和初始大小
        self.setWindowTitle("QSplitter 示例")
        self.resize(600, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
