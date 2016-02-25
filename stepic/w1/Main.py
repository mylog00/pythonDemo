# coding=utf-8
num = input()
num = list(num)
a = int(num[0])
a += int(num[1])
a += int(num[2])

b = int(num[3])
b += int(num[4])
b += int(num[5])

if a == b:
    print('Счастливый')
else:
    print('Обычный')
