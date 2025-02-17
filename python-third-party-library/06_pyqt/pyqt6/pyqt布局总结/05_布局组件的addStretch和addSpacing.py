import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("addStretch 和 addSpacing 示例")
        self.setGeometry(100, 100, 300, 200)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # 第一个按钮，直接添加到布局中
        button1 = QPushButton("Button 1")
        layout.addWidget(button1)

        # 使用 addSpacing 添加固定间距
        # layout.addSpacing(20)  # 添加 20 像素的固定间距

        # 第二个按钮，添加到布局中
        button2 = QPushButton("Button 2")
        layout.addWidget(button2)

        # 使用 addStretch 添加弹性间距
        layout.addStretch(1)  # 添加一个弹性空间，占据剩余空间

        # 第三个按钮，添加到布局中
        button3 = QPushButton("Button 3")
        layout.addWidget(button3)

        # 将布局应用到窗口
        self.setLayout(layout)


# 创建应用程序和窗口
app = QApplication(sys.argv)
window = MyWindow()
window.show()

# 运行应用程序
sys.exit(app.exec())
