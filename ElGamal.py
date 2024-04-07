import random
from sympy import mod_inverse, isprime
import tkinter as tk
from tkinter import messagebox

def tao_khoa(p, g, x):
    """Tạo khóa công cộng và khóa riêng."""
    y = pow(g, x, p)  # Khóa công cộng
    return (y, x)

def tim_goc_nguyen_thuy(p):
    """Tìm gốc nguyên thủy theo modulo p."""
    if p == 2:
        return 1
    phi = p - 1
    for candidate in range(2, p):
        if pow(candidate, phi, p) == 1:
            return candidate
    return None

def tao_p_va_g():
    """Tạo một số nguyên tố ngẫu nhiên (p) và gốc nguyên thủy tương ứng (g)."""
    p = random.randint(1000, 10000)
    while not isprime(p):
        p = random.randint(1000, 10000)
    g = tim_goc_nguyen_thuy(p)
    if g is not None:
        p_nhap.delete(0, tk.END)
        p_nhap.insert(0, str(p))
        g_nhap.delete(0, tk.END)
        g_nhap.insert(0, str(g))
        messagebox.showinfo("Thành công", "Số nguyên tố ngẫu nhiên (p) và gốc nguyên thủy (g) đã được tạo thành công!")
    else:
        messagebox.showerror("Lỗi", "Không thể tìm gốc nguyên thủy cho số nguyên tố đã tạo (p).")

def ma_hoa_ky_tu(ky_tu, p, g, y):
    """Mã hóa một ký tự sử dụng ElGamal."""
    chu_cai = ord(ky_tu)  # Giá trị ASCII của ký tự
    k = random.randint(1, p - 2)  # Tạo một khóa ngẫu nhiên
    c1 = pow(g, k, p)
    s = pow(y, k, p)
    c2 = (chu_cai * s) % p
    return (c1, c2)

def giai_ma_ky_tu(ky_tu_ma_hoa, p, x):
    """Giải mã một ký tự đã được mã hóa bằng ElGamal."""
    c1, c2 = ky_tu_ma_hoa
    s = pow(c1, x, p)
    nghich_dao_s = mod_inverse(s, p)
    if nghich_dao_s is None:
        raise ValueError(f"Nghịch đảo của {s} (mod {p}) không tồn tại")
    chu_cai = (c2 * nghich_dao_s) % p
    return chr(chu_cai)

def giai_ma_van_ban(van_ban_ma_hoa, p, x):
    """Giải mã một chuỗi đã được mã hóa bằng ElGamal."""
    van_ban_giai_ma = ""
    for ky_tu_ma_hoa in van_ban_ma_hoa:
        ky_tu = giai_ma_ky_tu(ky_tu_ma_hoa, p, x)
        van_ban_giai_ma += ky_tu
    return van_ban_giai_ma

def tao_so_nguyen_to():
    """Tạo một số nguyên tố ngẫu nhiên."""
    p = random.randint(1000, 10000)
    while not isprime(p):
        p = random.randint(1000, 10000)
    return p

def ma_hoa_giai_ma():
    """Mã hóa hoặc giải mã văn bản đầu vào dựa trên các tham số do người dùng cung cấp."""
    try:
        p = int(p_nhap.get())
        g = int(g_nhap.get())
        van_ban_goc = van_ban_nhap.get()
        x = random.randint(2, p - 2)
        y, _ = tao_khoa(p, g, x)
        van_ban_ma_hoa = [ma_hoa_ky_tu(ky_tu, p, g, y) for ky_tu in van_ban_goc]
        van_ban_giai_ma = giai_ma_van_ban(van_ban_ma_hoa, p, x)
        ket_qua.config(text=f"Mã hóa: {van_ban_ma_hoa}\nGiải mã: '{van_ban_giai_ma}'")
        messagebox.showinfo("Thành công", "Mã hóa và giải mã hoàn tất thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def xoa_ket_qua():
    """Xóa nhãn kết quả."""
    ket_qua.config(text="")

# Tạo cửa sổ tkinter
cua_so = tk.Tk()
cua_so.title("Mã Hóa ElGamal")

# Nhãn và ô nhập cho p
p_nhap_label = tk.Label(cua_so, text="Nhập một số nguyên tố lớn (p):")
p_nhap_label.grid(row=0, column=0, padx=5, pady=5)
p_nhap = tk.Entry(cua_so)
p_nhap.grid(row=0, column=1, padx=5, pady=5)

# Nút để tạo số nguyên tố ngẫu nhiên
nut_tao_so_nguyen_to_ngau_nhien = tk.Button(cua_so, text="Tạo Số Nguyên Tố Ngẫu Nhiên", command=tao_so_nguyen_to)
nut_tao_so_nguyen_to_ngau_nhien.grid(row=0, column=2, padx=5, pady=5)

# Nhãn và ô nhập cho g
g_nhap_label = tk.Label(cua_so, text="Nhập một gốc nguyên thủy modulo p (g):")
g_nhap_label.grid(row=1, column=0, padx=5, pady=5)
g_nhap = tk.Entry(cua_so)
g_nhap.grid(row=1, column=1, padx=5, pady=5)

# Nút tạo ngẫu nhiên
nut_tao_ngau_nhien = tk.Button(cua_so, text="Tạo Ngẫu Nhiên", command=tao_p_va_g)
nut_tao_ngau_nhien.grid(row=1, column=2, padx=5, pady=5)

# Nhãn và ô nhập cho văn bản gốc
van_ban_nhap_label = tk.Label(cua_so, text="Nhập văn bản:")
van_ban_nhap_label.grid(row=2, column=0, padx=5, pady=5)
van_ban_nhap = tk.Entry(cua_so)
van_ban_nhap.grid(row=2, column=1, padx=5, pady=5)

# Nút để mã hóa/giải mã
nut_ma_hoa_giai_ma = tk.Button(cua_so, text="Mã Hóa/Giải Mã", command=ma_hoa_giai_ma)
nut_ma_hoa_giai_ma.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Nút để xóa kết quả
nut_xoa_ket_qua = tk.Button(cua_so, text="Xóa Kết Quả", command=xoa_ket_qua)
nut_xoa_ket_qua.grid(row=3, column=2, padx=5, pady=5)

# Nhãn để hiển thị kết quả
ket_qua = tk.Label(cua_so, text="", wraplength=300)
ket_qua.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Chạy vòng lặp sự kiện của tkinter
cua_so.mainloop()
