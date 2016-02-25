n = int(input())
x = 0
y = 0
while n > 0:
    cmd = input().strip().split()
    vector = cmd[0]
    value = int(cmd[1])
    if vector == 'север':
        y += value
    elif vector == 'юг':
        y -= value
    elif vector == 'восток':
        x += value
    else:
        x -= value
    n -= 1
print(x, y, sep=' ')
