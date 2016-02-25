path = 'task8.txt'
math_avr = 0
physics_avr = 0
russian_avr = 0
counter = 0
with open(path, 'r') as fr:
    for line in fr:
        s = line.strip().split(';')
        print((int(s[1]) + int(s[2]) + int(s[3]))/3)
        math_avr += int(s[1])
        physics_avr += int(s[2])
        russian_avr += int(s[3])
        counter += 1

print(math_avr/counter, physics_avr/counter, russian_avr/counter, sep=' ')
