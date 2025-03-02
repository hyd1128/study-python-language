#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys

from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QApplication


class ControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.v_box_layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        self.list_widget.addItem('item1')
        self.list_widget.addItem(QListWidgetItem('item2'))
        QListWidgetItem('item3', self.list_widget)
        self.v_box_layout.addWidget(self.list_widget, stretch=1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ControllerWidget()
    w.show()
    sys.exit(app.exec())


