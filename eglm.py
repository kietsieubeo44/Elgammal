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

# Sử dụng
public_key, private_key = generate_keypair()
plaintext = 123 # Văn bản cần mã hóa
print("Văn bản ban đầu:", plaintext)
ciphertext = encrypt(public_key, plaintext)
print("Văn bản sau khi mã hóa:", ciphertext)
decrypted_text = decrypt(private_key, public_key, ciphertext)
print("Văn bản sau khi giải mã:", decrypted_text)
