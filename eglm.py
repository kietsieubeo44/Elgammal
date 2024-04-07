import random
from sympy import mod_inverse

def generate_keys(p, g, x):
    """Tạo khóa công khai và khóa riêng tư"""
    y = pow(g, x, p)  # Khóa công khai
    return (y, x)

def encrypt(plaintext, p, g, y):
    """Mã hóa văn bản thô bằng ElGamal"""
    k = random.randint(1, p - 2)  # Tạo khóa ngẫu nhiên
    c1 = pow(g, k, p)
    s = pow(y, k, p)
    c2 = (plaintext * s) % p
    return (c1, c2)

def decrypt(ciphertext, p, x):
    """Giải mã văn bản mã hóa bằng ElGamal"""
    c1, c2 = ciphertext
    s = pow(c1, x, p)
    plaintext = (c2 * mod_inverse(s, p)) % p
    return plaintext

def main():
    # Nhập số nguyên tố lớn p và số nguyên g
    p = int(input("Nhập số nguyên tố lớn p: "))
    g = int(input("Nhập số nguyên g (primitive root modulo p): "))
    
    # Sinh khóa riêng tư và công khai
    x = random.randint(2, p - 2)  # Khóa riêng tư
    y, _ = generate_keys(p, g, x)   # Khóa công khai
    
    print("Khóa công khai (y):", y)
    print("Khóa riêng tư (x):", x)
    
    # Nhập và mã hóa văn bản thô
    while True:
        try:
            plaintext = int(input("Nhập văn bản thô cần mã hóa: "))
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên.")
    
    ciphertext = encrypt(plaintext, p, g, y)
    print("Văn bản đã mã hóa:", ciphertext)
    
    # Giải mã văn bản mã hóa
    decrypted_text = decrypt(ciphertext, p, x)
    print("Văn bản đã giải mã:", decrypted_text)

if __name__ == "__main__":
    main()
