s = input()

seq = [int(i) for i in s.split()]
seq.sort()

prev = seq[0]
count = 1
res = ''
for i in seq[1:]:
    if i == prev:
        count += 1
    elif count > 1:
        res += str(prev) + ' '
        count = 1
        prev = i
    else:
        count = 1
        prev = i
if count > 1:
    res += str(prev) + ' '
print(res)
