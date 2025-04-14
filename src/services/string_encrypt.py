import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.A51 import A51Cipher
from utils.check_input import check_character, check_key_arr

class StringEncrypt:
    @staticmethod 
    def encrypt(keyArr, string_input):

        for word in string_input:
            if word == " ":
                continue
            if not check_character(word):
                print(f"Chữ {word} vượt quá 8 chữ cái đầu tiên (A-H).")
                return {"message": f"Chữ {word} vượt quá 8 ký tự đầu tiên.", "status": False}

        process_details = []
        process_details.append(f"Chi tiết mã hóa:")
        encrypted_chars = set()
        encrypted_string = ""
        for s in string_input:
            # ma hoa tung chu
            if s == " ":
                encrypted_string += s
                continue
            encrypted_word = A51Cipher.encrypt(keyArr=keyArr,character=s)
            encrypted_string += encrypted_word

            if s not in encrypted_chars:
                encrypted_chars.add(s)
                process_details.append(f"{s} -> {encrypted_word}")
            
        return {"result_string": encrypted_string, "process_details": process_details, "status": True}
    
def main():
    plain_text = input('Nhập bản rõ (A-H): ').strip().upper()

    for word in plain_text:
        if not check_character(character=word):
            print('Chỉ nhập ký tự từ A-H')
            return  # Thoát luôn, không làm ăn gì nữa

    key_str = input('Enter key (23 ký tự 0 hoặc 1): ').strip()

    try:
        key_arr = [int(x) for x in key_str]
    except ValueError:
        print("Key chỉ được chứa các số 0 hoặc 1.")
        return

    if not check_key_arr(key_arr=key_arr):
        print("Khóa phải có 23 ký tự và chỉ chứa 0 hoặc 1.")
        return

    # Mã hóa
    result = StringEncrypt.encrypt(keyArr=key_arr, string_input=plain_text)
    encrypted_string = result['result_string']
    process_details = result['process_details']

    # In kết quả
    print(f"\nKết quả mã hóa: {encrypted_string}")
    print(f"\nKhóa mã hóa: {key_str}")
    print(f"\nGiải thích chi tiết: {process_details}")

if __name__ == '__main__':
    main()
