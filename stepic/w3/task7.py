m = dict()
with open('task7.txt', 'r') as fr:
    for line in fr:
        s = line.strip().split()
        for i in s:
            i = i.lower()
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

max_count = max(m.values())
titles = []
for k, v in m.items():
    if v == max_count:
        titles.append(k)
titles = sorted(titles)
res = titles[0]
print(res, m.get(res), sep=' ')
