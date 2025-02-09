import math

# 1
# degree = int(input('Input degree: '))
# print(f'Output radian: {math.radians(degree)}')


# 2
def area_of_trapezoid(h, a, b):
    s = (a+b)*h * 0.5
    return s

# h = int(input('Height: '))
# a = int(input('Base, first value: '))
# b = int(input('Base, first value: '))

# print(f'Area of a trapezoid: {area_of_trapezoid(h, a, b)}')


# 3
def area_of_polygon(n, a):
    s = int((n * a**2) / (4 * math.tan(math.pi / n)))
    return s

# n = int(input('Input number of sides: '))
# a = int(input('Input the length of a side: '))

# print(f'Area of a polygon: {area_of_polygon(n, a)}')


# 4
def area_of_parallelogram(a, h):
    s = a*h
    return s

# a = int(input('Length of base: '))
# h = int(input('Height of parallelogram: '))

# print(f'Area of a polygon: {area_of_parallelogram(a, h):.1f}')