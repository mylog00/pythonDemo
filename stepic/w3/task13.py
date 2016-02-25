d = int(input())
words = set()
while d > 0:
    words.add(input().strip().lower())
    d -= 1
l = int(input())
res = set()
while l > 0:
    strings = input().lower().split()
    for string in strings:
        if string not in words:
            res.add(string)
    l -= 1
for s in res:
    print(s)
