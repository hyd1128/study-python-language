#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSizePolicy

"""
 水平布局同理
"""

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("QVBoxLayout 示例")
        self.setFixedSize(800, 600)  # 里面填写的数值是像素

        # 创建 QVBoxLayout 布局
        layout = QVBoxLayout()

        """
    QSizePolicy 提供了几种策略，常见的有：
    
    Fixed：固定大小，不允许伸缩。
    Preferred：推荐大小，允许控件根据内容或父容器的空间适当调整大小。
    Expanding：控件会扩展以填满可用空间。
    Minimum：控件大小会尽量缩小，但保持至少最小尺寸。
    Maximum：控件可以伸展到最大的尺寸。
        """

        # 创建几个按钮，并添加到布局中
        button1 = QPushButton("按钮 1")
        button2 = QPushButton("按钮 2")
        button3 = QPushButton("按钮 3")
        button4 = QPushButton("按钮 4")
        button5 = QPushButton("按钮 5")

        # 占用位置的优先级: Expanding > Preferred = Maximum > Minimum > Fixed
        button1.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        button2.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        button3.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        button4.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        button5.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        # 设置窗口的布局
        self.setLayout(layout)


# 启动应用程序
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
