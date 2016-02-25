a = open('task6out.txt', 'w')
with open('task6.txt', 'r') as fr:
    s = fr.readline().strip()
    i = 0
    j = 1
    while j < len(s):
        while j < len(s) and s[j].isnumeric():
            j += 1
        letter = s[i]
        number = int(s[i + 1:j])
        while number > 0:
            a.write(letter)
            number -= 1
        i = j
        j = i + 1
a.close()
