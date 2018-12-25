a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Phuong trinh vo nghiem.")
elif delta == 0:
    x = -b / (2*a)
    print("Phuong trinh co 1 nghiem x =", x)
else:
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    print("Phuong trinh co 2 nghiem x1 =", x1,"va x2 =", x2)
