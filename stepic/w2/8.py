# coding=utf-8
s = input()
num = int(input())
seq = [int(i) for i in s.split()]
res = ''

for i in range(len(seq)):
    if seq[i] == num:
        res += str(i) + " "
if len(res) > 0:
    print(res)
else:
    print("Отсутствует")
