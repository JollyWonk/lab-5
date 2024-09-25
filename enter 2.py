import math

R1 = float(input("Введiть внутрiшнiй радiус R1: "))
R2 = float(input("Введiть внутрiшнiй радiус R2: "))

x = float(input("Введiть координату x: "))
y = float(input("Введiть координату y: "))

distance = math.sqrt(x**2 + y**2)

if R2 < distance < R1:
    print("Точка належить кiльцу.")
else:
    print("Точка не належить кiльцу.")
