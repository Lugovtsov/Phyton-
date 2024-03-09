import math

r = int(input("Введите радиус круга: "))
h = int(input("Введите высоту цилиндра: "))

s = math.pi * r**2
v = s * h 

print(round(v, 2))