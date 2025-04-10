class A5_1:
    def __init__(self, key):
        self.reg_x = [0] * 19
        self.reg_y = [0] * 22
        self.reg_z = [0] * 23
        self.load_key(key)

    def load_key(self, key):
        key_bits = [int(bit) for bit in format(key, '064b')]
        for i in range(19):
            self.reg_x[i] = key_bits[i]
        for i in range(22):
            self.reg_y[i] = key_bits[i + 19]
        for i in range(23):
            self.reg_z[i] = key_bits[i + 41]

    def majority(self, x, y, z):
        return (x & y) | (x & z) | (y & z)

    def clock(self):
        maj = self.majority(self.reg_x[8], self.reg_y[10], self.reg_z[10])
        if self.reg_x[8] == maj:
            new_bit_x = self.reg_x[13] ^ self.reg_x[16] ^ self.reg_x[17] ^ self.reg_x[18]
            self.reg_x = [new_bit_x] + self.reg_x[:-1]
        if self.reg_y[10] == maj:
            new_bit_y = self.reg_y[20] ^ self.reg_y[21]
            self.reg_y = [new_bit_y] + self.reg_y[:-1]
        if self.reg_z[10] == maj:
            new_bit_z = self.reg_z[7] ^ self.reg_z[20] ^ self.reg_z[21] ^ self.reg_z[22]
            self.reg_z = [new_bit_z] + self.reg_z[:-1]

    def generate_keystream(self, length):
        keystream = []
        for _ in range(length):
            self.clock()
            key_bit = self.reg_x[-1] ^ self.reg_y[-1] ^ self.reg_z[-1]
            keystream.append(key_bit)
        return keystream

    def encrypt(self, plaintext):
        plaintext_bits = [int(bit) for bit in
                          format(int.from_bytes(plaintext.encode(), 'big'), f'0{len(plaintext) * 8}b')]
        keystream = self.generate_keystream(len(plaintext_bits))
        ciphertext_bits = [p ^ k for p, k in zip(plaintext_bits, keystream)]
        return ''.join(map(str, ciphertext_bits))

    def decrypt(self, ciphertext_bits):
        keystream = self.generate_keystream(len(ciphertext_bits))
        plaintext_bits = [int(c) ^ k for c, k in zip(ciphertext_bits, keystream)]
        plaintext_bytes = int(''.join(map(str, plaintext_bits)), 2).to_bytes(len(plaintext_bits) // 8, 'big')
        return plaintext_bytes.decode()


# Ví dụ sử dụng
key = 0x123456789ABCDEF  # Khóa 64-bit
cipher = A5_1(key)
plaintext = "C"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted:", decrypted_text)
