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

from A51Cipher_character import A51Cipher
from A51Cipher_string import StringEncrypt

class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("A5/1 Cipher")
        self.setGeometry(100, 100, 400, 450)

        layout = QVBoxLayout()

        # ban ro
        self.plain_text_label = QLabel("Nhập ký tự cần mã hóa:")
        layout.addWidget(self.plain_text_label)

        self.plain_text_input = QLineEdit()
        self.plain_text_input.setFixedWidth(200)
        layout.addWidget(self.plain_text_input)

        # khoa ma hoa
        self.key_label = QLabel("Nhập vào khóa mã khóa:")
        layout.addWidget(self.key_label)

        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        # ma hoa
        self.encryptButton = QPushButton("Mã hóa")
        self.encryptButton.setFixedWidth(100)
        self.encryptButton.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encryptButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.resultLabel = QLabel("Kết quả: ")
        self.resultLabel.setEnabled(False)
        layout.addWidget(self.resultLabel)

        self.detailEncryptBtn = QPushButton("Xem chi tiết mã hóa")
        self.detailEncryptBtn.clicked.connect(self.show_details)
        self.detailEncryptBtn.hide()
        layout.addWidget(self.detailEncryptBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        # hien thi khoa ma hoa
        self.encryptKeyLbl = QLabel("Khóa mã hóa: ")
        self.encryptKeyLbl.hide()
        layout.addWidget(self.encryptKeyLbl)
        
        # giai ma
        self.decodeBtn = QPushButton("Giải mã")
        self.decodeBtn.setFixedWidth(100)
        self.decodeBtn.clicked.connect(self.decode_text)
        self.decodeBtn.hide()
        layout.addWidget(self.decodeBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.decodingResultLbl = QLabel("Kết quả giải mã: ")
        # self.decodingResultLbl.setEnabled(False)
        layout.addWidget(self.decodingResultLbl)

        self.detailDecodeBtn = QPushButton("Xem chi tiết giải mã")
        self.detailDecodeBtn.clicked.connect(self.show_decode_details)
        self.detailDecodeBtn.hide()
        layout.addWidget(self.detailDecodeBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

        self.encryption_details = []
        self.encryption_details_text = ""
        self.decode_details = []
        self.decode_details_text = ""

    # Ma hoa
    def encrypt_text(self):
        input_char = self.plain_text_input.text().strip()
        if len(input_char) != 1 or not input_char.isalpha():
            self.resultLabel.setText("Vui lòng nhập một ký tự là chữ cái!")
            return

        key_arr_str = self.key_input.text().strip()

        # kiem tra dinh dang khoa ma hoa
        if not re.fullmatch(r"[01]+", key_arr_str):
            self.resultLabel.setText("Khóa mã hóa phải là chuỗi nhị phân.")
            return
        
        # kiem tra do dai khoa ma hoa
        if len(key_arr_str) != 23:
            self.resultLabel.setText("Khóa mã hóa phải có độ dài bằng 23.")
            return
        
        # tao khoa
        key_arr = [int(bit) for bit in key_arr_str]

        # ma hoa
        cipher = A51Cipher(key_arr)
        encrypted_char, self.encryption_details = cipher.encrypt(input_char)

        self.encryption_details_text = "\n"

        # hien thi cac noi dung da an
        self.resultLabel.setEnabled(True)
        self.resultLabel.setText(f"Kết quả mã hóa: {encrypted_char}")
        self.detailEncryptBtn.show()
        self.encryptKeyLbl.setText("Khóa mã hóa: " + self.key_input.text().strip())
        self.encryptKeyLbl.show()

        self.decodeBtn.show()

    # hien thi chi tiet ma hoa
    def show_details(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Chi tiết mã hóa")
        msg_box.setText("\n".join(self.encryption_details))
        msg_box.setMinimumHeight(200)
        msg_box.exec()
        # QMessageBox.information(self, "", "\n".join(self.encryption_details))

    # giai ma
    def decode_text(self):
        # lay ky tu da ma hoa
        txt_res = self.resultLabel.text().strip()
        input_char = txt_res[-1]
        if not input_char:
            self.decodingResultLbl.setText("Bạn chưa mã hóa!")
            return
        
        # tao khoa
        key_str = self.key_input.text().strip()
        key_arr = [int (x) for x in key_str]
        
        # giai ma
        cipher = A51Cipher(key_arr)
        decoded_char, self.decode_details = cipher.decode_char(input_char)

        self.decode_details_text = "\n"

        self.decodingResultLbl.setText(f"Kết quả giải mã: {decoded_char}")
        self.detailDecodeBtn.show()

    # hien thi chi tiet giai ma
    def show_decode_details(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Chi tiết giải mã")
        msg_box.setText("\n".join(self.decode_details))
        msg_box.setMinimumHeight(200)
        msg_box.exec()       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CipherApp()
    window.show()
    sys.exit(app.exec())