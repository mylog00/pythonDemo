s = input()
a = []
n = 0
while s != 'end':
    a.append([int(i) for i in s.split()])
    n += 1
    s = input()

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == 0:
            i_prev = a[-1][j]
        else:
            i_prev = a[i-1][j]

        if i == len(a) - 1:
            i_nxt = a[0][j]
        else:
            i_nxt = a[i + 1][j]
        if j == 0:
            j_prev = a[i][-1]
        else:
            j_prev = a[i][j-1]

        if j == len(a[i]) - 1:
            j_nxt = a[i][0]
        else:
            j_nxt = a[i][j+1]

        res = i_prev+i_nxt+j_prev+j_nxt
        print(res, end=' ')
    print('')
