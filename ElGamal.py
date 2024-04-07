import random
from sympy import mod_inverse, isprime
import tkinter as tk

def generate_keys(p, g, x):
    """Tạo khóa công khai và khóa riêng tư"""
    y = pow(g, x, p)  # Khóa công khai
    return (y, x)

def encrypt_char(char, p, g, y):
    """Mã hóa một ký tự bằng ElGamal"""
    plaintext = ord(char)  # Mã ASCII của ký tự
    k = random.randint(1, p - 2)  # Tạo khóa ngẫu nhiên
    c1 = pow(g, k, p)
    s = pow(y, k, p)
    c2 = (plaintext * s) % p
    return (c1, c2)

def decrypt_char(ciphertext, p, x):
    """Giải mã một ký tự mã hóa bằng ElGamal"""
    c1, c2 = ciphertext
    s = pow(c1, x, p)
    inverse_s = mod_inverse(s, p)
    if inverse_s is None:
        raise ValueError(f"Inverse of {s} (mod {p}) does not exist")
    plaintext = (c2 * inverse_s) % p
    return chr(plaintext)  # Chuyển từ mã ASCII về ký tự


def decrypt_text(ciphertext, p, x):
    """Giải mã một chuỗi ký tự mã hóa bằng ElGamal"""
    decrypted_text = ""
    for char_ciphertext in ciphertext:
        char = decrypt_char(char_ciphertext, p, x)
        decrypted_text += char
    return decrypted_text

def generate_prime():
    """Tạo số nguyên tố ngẫu nhiên"""
    while True:
        p = random.randint(1000, 10000)
        if isprime(p):
            return p

def encrypt_decrypt():
    p = int(p_entry.get())
    g = int(g_entry.get())
    plaintext = plaintext_entry.get()
    x = random.randint(2, p - 2)
    y, _ = generate_keys(p, g, x)
    ciphertext = [encrypt_char(char, p, g, y) for char in plaintext]
    decrypted_text = decrypt_text(ciphertext, p, x)
    result_label.config(text=f"Mã hóa: {ciphertext}\nGiải mã: '{decrypted_text}'")

# Tạo cửa sổ
window = tk.Tk()
window.title("ElGamal Encryption")

# Nhãn và ô nhập cho p
p_label = tk.Label(window, text="Nhập số nguyên tố lớn p:")
p_label.grid(row=0, column=0, padx=5, pady=5)
p_entry = tk.Entry(window)
p_entry.grid(row=0, column=1, padx=5, pady=5)

# Nút tạo số nguyên tố ngẫu nhiên
random_prime_button = tk.Button(window, text="Tạo số nguyên tố ngẫu nhiên", command=generate_prime)
random_prime_button.grid(row=0, column=2, padx=5, pady=5)

# Nhãn và ô nhập cho g
g_label = tk.Label(window, text="Nhập số nguyên g (primitive root modulo p):")
g_label.grid(row=1, column=0, padx=5, pady=5)
g_entry = tk.Entry(window)
g_entry.grid(row=1, column=1, padx=5, pady=5)

# Nhãn và ô nhập cho văn bản thô
plaintext_label = tk.Label(window, text="Nhập văn bản thô cần mã hóa:")
plaintext_label.grid(row=2, column=0, padx=5, pady=5)
plaintext_entry = tk.Entry(window)
plaintext_entry.grid(row=2, column=1, padx=5, pady=5)

# Nút thực hiện mã hóa và giải mã
encrypt_button = tk.Button(window, text="Mã hóa/Giải mã", command=encrypt_decrypt)
encrypt_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Nhãn để hiển thị kết quả
result_label = tk.Label(window, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
