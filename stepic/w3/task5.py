def f(x):
    return x * 2

n = int(input())
m = dict()
while n > 0:
    i = int(input())
    if i not in m:
        m[i] = f(i)

    print(m.get(i))
    n -= 1
