# coding=utf-8
figure = input()
if figure == "круг":
    r = int(input())
    pi = 3.14
    print(pi * r * r)
elif figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2.0
    p *= (p - a) * (p - b) * (p - c)
    print(p ** 0.5)
else:
    w = int(input())
    h = int(input())
    print(w * h)
