# LCM (НОК)
a = int(input())
b = int(input())

m = a * b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(m // (a + b))
