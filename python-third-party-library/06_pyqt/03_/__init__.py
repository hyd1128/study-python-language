# #!/usr/bin/env python
# # _*_ coding: utf-8 _*_
# # @Time : 2024/11/1 17:36
# # @Author : limber
# # @desc :
#
# """
#  创建一个小案例 使用使用qthread创建一个自定义信号，实时发送数据出去
#
#  创建一个页面，在页面点击按钮，启动qthread qthread输出的信息输入到textbrower上


import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import QApplication, QTextBrowser
from thread_one import ThreadOne


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # 创建一个线程
        self.message_thread = ThreadOne()
        self.message_thread.signal.connect(self.send_data)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Form")
        self.resize(688, 446)
        self.horizontalLayout_ = QtWidgets.QHBoxLayout(self)

        self.widget = QtWidgets.QWidget(parent=self)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_2)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton.setText("下载app")
        self.pushButton_5.setText("停止")

        # 绑定槽函数
        self.pushButton.clicked.connect(self.start_thread)
        self.pushButton_5.clicked.connect(self.stop_thread)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_2)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_2)
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_2.setText("删除app")
        self.pushButton_6.setText("停止")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_2)
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget_2)
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_3.setText("更新app")
        self.pushButton_7.setText("停止")

        self.horizontalLayout_4.addWidget(self.widget_2)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.widget)
        self.horizontalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_.addWidget(self.widget)

    # 启动线程
    def start_thread(self):
        if not self.message_thread.isRunning():  # 使用 isRunning 检查线程状态
            self.message_thread.flag = True
            self.message_thread.start()

    # 停止线程
    def stop_thread(self):
        if self.message_thread.flag:
            self.message_thread.stop()

    # 将数据实时发送到 textBrowser
    def send_data(self, msg: str):
        self.textBrowser.append(msg)
        self.textBrowser.moveCursor(QTextCursor.MoveOperation.End)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
