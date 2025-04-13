class A51Cipher:
    @staticmethod
    def encrypt(keyArr, character):
        if character not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            return {"message": f"{character} vượt quá 8 chữ cái đầu tiên (A-H)", "status": False}
        
        # chuyen ky tu thanh bit nhi phan
        index = ord(character) - 41
        bitInput = [(index >> i) & 1 for i in range(2, -1, -1)]

        # khoi tao cac thanh ghi X, Y, Z
        X, Y, Z = keyArr[:6], keyArr[6:14], keyArr[14:]

        # sinh key bit (s)
        s = []
        for i in range(3):
            current_registers = f"X: {X} \nY: {Y} \nZ: {Z} \n";
            m = (X[1] + Y[3] + Z[3]) >= 2

            if X[1] == m:
                X = [X[2] ^ X[4] ^ X[5]] + X[:-1]
            if Y[3] == m:
                Y = [Y[6] ^ Y[7]] + Y[:-1]
            if Z[3] == m:
                Z = [Z[2] ^ Z[7] ^ Z[8]] + Z[:-1]

            s_bit = X[5] ^ Y[7] ^ Z[8]
            s.append(s_bit)

        # XOR voi bitInput de sinh ket qua
        res = [bitInput[i] ^ s[i] for i in range(3)]

        # chuyen tu 3 bit ve ky tu
        indexResult = sum(res[i] * (1 << (2-i)) for i in range(3))
        encrypted_char = chr(ord('A') + indexResult)


        return encrypted_char