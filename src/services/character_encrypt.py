import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.check_input import check_character, check_key_arr
class A51Cipher:
    @staticmethod
    def encrypt(keyArr, character):
        if not check_character(character=character):
            return {"message": f"{character} vượt quá 8 chữ cái đầu tiên (A-H)", "status": False}
        
        # chuyen ky tu thanh bit nhi phan
        index = ord(character) - 41
        bitInput = [(index >> i) & 1 for i in range(2, -1, -1)]

        # khoi tao cac thanh ghi X, Y, Z
        X, Y, Z = keyArr[:6], keyArr[6:14], keyArr[14:]

        # luu qua trinh ma hoa de hien thi chi tiet
        process_details = []

        process_details.append(f"Bản rõ {character} -> " + "".join(str(bit) for bit in bitInput) + "\n")
        step_0 = (f"BƯỚC {0}: Khởi tạo\n X = {X} \n Y = {Y} \n Z = {Z} \n")
        process_details.append(step_0)

        # sinh key bit (s)
        s = []
        for i in range(3):
            current_registers = f"X: {X} \nY: {Y} \nZ: {Z} \n";
            logs = []
            m = (X[1] + Y[3] + Z[3]) >= 2
            logs.append(f"\nm = X[1] + Y[3] + Z[3] >= 2? -> m = {int(m)}\n")

            if X[1] == m:
                X = [X[2] ^ X[4] ^ X[5]] + X[:-1]
                logs.append(f"X[1] = m -> Quay X: {X}")
            else: 
                logs.append(f"X[1] != m -> Giữ nguyên: X = {X}")
            if Y[3] == m:
                Y = [Y[6] ^ Y[7]] + Y[:-1]
                logs.append(f"Y[3] = m -> Quay Y: {Y}")
            else:
                logs.append(f"Y[3] != m -> Giữ nguyên: {Y}")
            if Z[3] == m:
                Z = [Z[2] ^ Z[7] ^ Z[8]] + Z[:-1]
                logs.append(f"Z[3] = m -> Quay Z: {Z}")
            else:
                logs.append(f"Z[3] != m -> Giữ nguyên: {Z}")

            s_bit = X[5] ^ Y[7] ^ Z[8]
            s.append(s_bit)
            logs.append(f"\ns[{i}] = X[5] ^ Y[7] ^ Z[8] = {s_bit}")

            # ghi lai toan bo cac buoc
            process_details.append(f"BƯỚC {i+1}:\n" + current_registers + "\n".join(logs) + "\n")

        # XOR voi bitInput de sinh ket qua
        res = [bitInput[i] ^ s[i] for i in range(3)]

        # chuyen tu 3 bit ve ky tu
        indexResult = sum(res[i] * (1 << (2-i)) for i in range(3))
        encrypted_char = chr(ord('A') + indexResult)

        process_details.append(f"Vậy bản mã là: " + "".join(str(bit) for bit in res) + " ^ " + "".join(str(bit) for bit in s) + f" = {encrypted_char}")

        return {"result_character": encrypted_char, "process_details": process_details, "status": True} 
    

def main():
    character = input('Nhập bản rõ (A-H): ').strip().upper()

    if not check_character(character=character):
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
    result = A51Cipher.encrypt(keyArr=key_arr, character=character)
    encrypted_character = result['result_character']
    process_details = result['process_details']

    # In kết quả
    print(f"\nKết quả mã hóa: {encrypted_character}")
    print(f"\nKhóa mã hóa: {key_str}")
    print(f"\nGiải thích chi tiết: {process_details}")

if __name__ == '__main__':
    main()
