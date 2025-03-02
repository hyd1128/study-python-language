#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# !/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys

from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QApplication, QTableWidget


class ControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.v_box_layout = QVBoxLayout(self)

        # 实例化QTableWidget
        # 方式1: 在实例化类是床底行列参数
        # self.tableWidget = QTableWidget(5, 4)

        # 方式2: 先实例化类, 再调整表格的大小
        self.tableWidget = QTableWidget()

        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)

        self.v_box_layout.addWidget(self.tableWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ControllerWidget()
    w.show()
    sys.exit(app.exec())
