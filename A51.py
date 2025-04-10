
class A51Cipher:
    def __init__(self, keyArr):
        self.X = keyArr[:6]
        self.Y = keyArr[6:14]
        self.Z = keyArr[14:]

    def turn_X(self):
       self.X = [self.X[2] ^ self.X[4] ^ self.X[5]] + self.X[:-1]
     
    def turn_Y(self):
        self.Y = [self.Y[6] ^ self.Y[7]] + self.Y[:-1]

    def turn_Z(self):
        self.Z = [self.Z[2] ^ self.Z[7] ^ self.Z[8]] + self.Z[:-1]

    @staticmethod
    def maj(x, y, z):
        return 1 if (x + y + z) >= 2 else 0

    @staticmethod
    def convert_text_to_binary_bits(character):
        bitArr = [0] * 3
        index = ord(character) - 41
        for i in range(3):
            temp = index // (2 ** (2 - i))
            bitArr[i] = temp % 2
        return bitArr

    def encrypt(self, character):
        bitInput = self.convert_text_to_binary_bits(character)
        s = [0] * 3
        res = [0] * 3

        for i in range(3):
            m = self.maj(self.X[1], self.Y[3], self.Z[3])
            if self.X[1] == m:
                self.turn_X()
            if self.Y[3] == m:
                self.turn_Y()
            if self.Z[3] == m:
                self.turn_Z()
            s[i] = self.X[5] ^ self.Y[7] ^ self.Z[8]

        for i in range(3):
            res[i] = bitInput[i] ^ s[i]

        indexResult = sum(res[i] * (2 ** (2 - i)) for i in range(3))
        characterRes = chr(ord('A') + indexResult)

        return characterRes