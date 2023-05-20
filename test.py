# Hàm tính toán delta
def delta(a, b, c, d):
    return 18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 - 27 * a ** 2 * d ** 2

# Hàm tính toán căn bậc 3 của một số
def cbrt(x):
    return x ** (1.0/3.0) if x > 0 else -(-x) ** (1.0/3.0)

# Hàm giải phương trình bậc 3
def cubic_equation(a, b, c, d):
    # Tính toán delta
    del_val = delta(a, b, c, d)
    
    # Tính toán các giá trị trong phương trình
    C = cbrt((del_val + (delta(a, b, c, d) ** 2 - 4 * delta(a, b, c, d) ** 3) ** 0.5) / 2.0)
    U = 1 + 1j * (3 ** 0.5)
    x1 = (-1 / (3 * a)) * (b + C + (b * U + c / (U * C)) / 3)
    x2 = (-1 / (3 * a)) * (b + (U * C + c / (U * C)) / 3 + C)
    x3 = (-1 / (3 * a)) * (b + (U * C + c / (U * C)) / 3 - C)
    
    # Trả về kết quả
    return [x1, x2, x3]

# Nhập các hệ số của phương trình bậc 3
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
d = float(input("Nhập hệ số d: "))

# Giải phương trình bậc 3
result = cubic_equation(a, b, c, d)

# In kết quả
print("Các nghiệm của phương trình là: ")
for i in range(len(result)):
    print("x{} = {}".format(i+1, result[i]))
