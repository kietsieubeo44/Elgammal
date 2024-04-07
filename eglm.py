import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    p = 761
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    return (p, g, h), x

def encrypt(public_key, plaintext):
    p, g, h = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (plaintext * pow(h, k, p)) % p
    return c1, c2

def decrypt(private_key, public_key, ciphertext):
    p, _, _ = public_key
    c1, c2 = ciphertext
    x = private_key
    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    plaintext = (c2 * s_inv) % p
    return plaintext

# Tạo khóa công khai và khóa riêng tư
public_key, private_key = generate_keypair()

# Nhập số nguyên bạn muốn mã hóa
plaintext = 123
print("Số nguyên ban đầu:", plaintext)

# Mã hóa số nguyên
ciphertext = encrypt(public_key, plaintext)
print("Số sau khi mã hóa:", ciphertext)

# Giải mã số nguyên bằng cách sử dụng khóa riêng tư
decrypted_text = decrypt(private_key, public_key, ciphertext)
print("Số sau khi giải mã:", decrypted_text)
