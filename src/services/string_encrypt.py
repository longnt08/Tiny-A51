from services.A51 import A51Cipher

class StringEncrypt:
    @staticmethod 
    def encrypt(keyArr, string_input):

        for word in string_input:
            if word == " ":
                continue
            if word not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
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
    
if __name__ == '__main__':
    keyArr = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]
    string_input = 'H'
    
    string_cipher = StringEncrypt()
    string_output = string_cipher.encrypt(keyArr, string_input)

    print(string_output)