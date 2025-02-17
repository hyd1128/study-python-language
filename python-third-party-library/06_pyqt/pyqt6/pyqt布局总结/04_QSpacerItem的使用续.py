import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy


class SpacerExample(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("QSpacerItem 示例")
        self.setGeometry(100, 100, 300, 200)

        # 创建垂直布局
        layout = QVBoxLayout()

        layout.setSpacing(0)
        # 设置布局的内边距为 0
        layout.setContentsMargins(0, 0, 0, 0)

        # 添加按钮1
        btn1 = QPushButton("按钮 1")
        btn1.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout.addWidget(btn1)

        # # 创建并添加一个垂直间距 (spacer)，使按钮之间有一定的空隙
        # spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        # layout.addItem(spacer)

        # 添加按钮2
        btn2 = QPushButton("按钮 2")
        btn2.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout.addWidget(btn2)

        # 设置布局到窗口
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpacerExample()
    window.show()
    sys.exit(app.exec())
