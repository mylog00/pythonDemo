string = input().split()
m = dict()
for s in string:
    s = s.lower()
    if s in m:
        m[s] = m.get(s) + 1
    else:
        m[s] = 1
for k, v in m.items():
    print(k, v)
