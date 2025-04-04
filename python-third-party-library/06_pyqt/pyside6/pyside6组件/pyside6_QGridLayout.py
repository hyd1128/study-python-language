#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLayoutItem, QSpacerItem, QSizePolicy, \
    QLabel, QHBoxLayout, QLineEdit, QTextBrowser, QPlainTextEdit


class GridLayoutDemo(QWidget):
    def __init__(self, parent=None):
        super(GridLayoutDemo, self).__init__(parent)
        grid = QGridLayout()
        self.setLayout(grid)

        # 添加行列标识
        for i in range(1, 8):
            rowEdit = QLineEdit('row%d' % (i))
            rowEdit.setReadOnly(True)
            grid.addWidget(rowEdit, i, 0)
            colEdit = QLineEdit('col%d' % (i))
            colEdit.setReadOnly(True)
            grid.addWidget(colEdit, 0, i)
        col_rol_Edit = QLineEdit('rol0_col0')
        col_rol_Edit.setReadOnly(True)
        grid.addWidget(col_rol_Edit, 0, 0, 1, 1)

        # 开始表演
        spacer = QSpacerItem(100, 70, QSizePolicy.Maximum)
        grid.addItem(spacer, 0, 0, 1, 1)
        grid.addWidget(QLabel('row1_col2_1_1'), 1, 2, 1, 1)
        grid.addWidget(QPushButton('row1_col3_1_1'), 1, 3, 1, 1)
        grid.addWidget(QPlainTextEdit('row2_col4_2_2'), 2, 4, 2, 2)
        grid.addWidget(QPlainTextEdit('row3_col2_2_2'), 3, 2, 2, 2)
        grid.addWidget(QPushButton('row5_col5_1_1'), 5, 5, 1, 1)
        spacer2 = QSpacerItem(100, 100, QSizePolicy.Maximum)
        grid.addItem(spacer2, 6, 5, 1, 2)
        grid.addWidget(QPushButton('row7_col6_1_1'), 7, 6, 1, 1)

        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('button_h1'))
        hlayout.addWidget(QPushButton('button_h2'))
        grid.addLayout(hlayout, 7, 1, 1, 2)

        grid.setColumnStretch(5, 1)
        grid.setColumnStretch(2, 1)
        grid.setColumnMinimumWidth(0, 80)

        self.move(300, 150)
        self.setWindowTitle('QGridLayout例子')

"""
如何计算网格大小:
    从控件的位置和跨度，我们可以推断出 QGridLayout 的行列数。例如：
行数：
最低行数是根据控件放置的最大行数来决定的。这里最大行数是 7，因为 QPushButton('row7_col6_1_1') 被放在第 7 行，所以网格至少有 8 行（行索引从 0 开始）。

列数：
最低列数是根据控件放置的最大列数来决定的。这里最大列数是 6，因为 QPushButton('row7_col6_1_1') 被放在第 6 列，所以网格至少有 7 列（列索引从 0 开始）。
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = GridLayoutDemo()
    demo.show()
    sys.exit(app.exec())
