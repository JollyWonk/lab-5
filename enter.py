import math

x = float(input("Введiть значеня х: "))
y = 0.0 

if x >= 0:
    y = x + 2 ** (x - 4) - math.sqrt(x)
elif -7.7 < x < 0:
    y = math.sin(2 * x) + math.log(abs(x))
else:
    y = math.cos(3 * x) - 1 / x

print("y =", y)
