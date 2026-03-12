a = float(input("Nhập chiều rộng a: "))
b = float(input("Nhập chiều dài b: "))
pi = 3.14
r = a / 2
dien_tich_hcn = a * b
dien_tich_tron = pi * r * r
dien_tich_trong_cay = dien_tich_hcn - dien_tich_tron
print(f"Diện tích trồng cây xung quanh: {round(dien_tich_trong_cay, 2)}")