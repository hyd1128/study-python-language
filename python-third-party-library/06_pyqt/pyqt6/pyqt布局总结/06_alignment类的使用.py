#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
import sys


class AlignmentDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alignment Flag Demo")
        self.setGeometry(100, 100, 600, 400)

        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 1. 文本对齐示例
        text_examples = QWidget()
        text_layout = QVBoxLayout(text_examples)

        # 左对齐文本
        left_label = QLabel("左对齐文本")
        left_label.setFrameStyle(QLabel.Shape.Box)
        left_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # 居中对齐文本
        center_label = QLabel("居中对齐文本")
        center_label.setFrameStyle(QLabel.Shape.Box)
        center_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 右对齐文本
        right_label = QLabel("右对齐文本")
        right_label.setFrameStyle(QLabel.Shape.Box)
        right_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # 垂直居中和水平居中组合
        vcenter_label = QLabel("垂直和水平居中")
        vcenter_label.setFrameStyle(QLabel.Shape.Box)
        vcenter_label.setMinimumHeight(50)
        vcenter_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        text_layout.addWidget(left_label)
        text_layout.addWidget(center_label)
        text_layout.addWidget(right_label)
        text_layout.addWidget(vcenter_label)

        # 2. 组件布局示例
        widget_examples = QWidget()
        widget_layout = QHBoxLayout(widget_examples)

        # 左侧组件
        left_widget = QLabel("左侧")
        left_widget.setFrameStyle(QLabel.Shape.Box)
        widget_layout.addWidget(left_widget, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # 中间组件
        center_widget = QLabel("中间")
        center_widget.setFrameStyle(QLabel.Shape.Box)
        widget_layout.addWidget(center_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        # 右侧组件
        right_widget = QLabel("右侧")
        right_widget.setFrameStyle(QLabel.Shape.Box)
        widget_layout.addWidget(right_widget, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        # 添加到主布局
        main_layout.addWidget(QLabel("文本对齐示例："))
        main_layout.addWidget(text_examples)
        main_layout.addWidget(QLabel("组件布局示例："))
        main_layout.addWidget(widget_examples)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlignmentDemo()
    window.show()
    sys.exit(app.exec())