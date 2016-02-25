num = int(input())
c = 1
res = ''
while num > 0:
    for i in range(c):
        if num > 0:
            res += str(c) + ' '
            num -= 1
        else:
            break
    c += 1

print(res)
