from src.services.A51 import A51Cipher

class StringEncrypt:
    @staticmethod 
    def encrypt(keyArr, string_input):
        cipher = A51Cipher(keyArr)

        encrypted_chars = [
            cipher.encrypt(s) if s != " " else " "
            for s in string_input
        ] 

        return "".join(encrypted_chars)
    
if __name__ == '__main__':
    keyArr = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0]
    string_input = 'H'
    
    string_cipher = StringEncrypt()
    string_output = string_cipher.encrypt(keyArr, string_input)

    print(string_output)