from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMainWindow, QApplication

class MyUserControl(QWidget):
    def __init__(self, text="Mặc định"):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel(text)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def setText(self, new_text):
        """Hàm để cập nhật nội dung của UserControl"""
        self.label.setText(new_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo UserControl PyQt6")
        self.setGeometry(100, 100, 400, 300)

        container = QWidget()
        layout = QVBoxLayout()

        # Thêm UserControl vào Form chính
        self.user_control_1 = MyUserControl("Hello, PyQt6!")
        layout.addWidget(self.user_control_1)

        self.user_control_2 = MyUserControl("UserControl thứ 2")
        layout.addWidget(self.user_control_2)

        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
