import math
x1 = int(input("Введите координату X первой точки:"))
y1 = int(input("Введите координату Y первой точки:"))
x2 = int(input("Введите координату X второй точки:"))
y2 = int(input("Введите координату Y второй точки:"))
R = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("Расстояние между двумя точками равно:", R)
