import sys
import re
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QVBoxLayout,
                             QMessageBox)

from PyQt6.QtCore import Qt

from A51Cipher_string import StringEncrypt

class CipherStringGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("String encryption")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        # ban ro
        self.plain_text_label = QLabel("Nhập chuỗi cần mã hóa (Tiếng Anh):")
        layout.addWidget(self.plain_text_label)

        self.plain_text_input = QLineEdit()
        layout.addWidget(self.plain_text_input)

        # khoa ma hoa
        self.key_label = QLabel("Nhập vào khóa mã hóa:")
        layout.addWidget(self.key_label)

        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        # nut ma hoa
        self.encrypt_button = QPushButton("Mã hóa")
        self.encrypt_button.setFixedWidth(100)
        self.encrypt_button.clicked.connect(self.encrypt_string)
        layout.addWidget(self.encrypt_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # hien thi ket qua
        self.result_label = QLabel("Kết quả: ")
        layout.addWidget(self.result_label)

        # xem chi tiet

        self.setLayout(layout)

    def encrypt_string(self):
        input_str = self.plain_text_input.text().strip()
        # character_list = list(input_str)

        key_input = self.key_input.text().strip()
        key_arr = list(map(int, list(key_input)))

        res = StringEncrypt.encrypt(key_arr, input_str)

        # hien thi ket qua
        self.result_label.setText(f"Kết quả:  {res}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CipherStringGUI()
    window.show()
    sys.exit(app.exec())