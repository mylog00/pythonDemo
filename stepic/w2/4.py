# dna = input()

dna = "aaaabbcaa"
prev = dna[0]
count = 1
res = ''
for i in dna[1:]:
    if i == prev:
        count += 1
    else:
        res += prev + str(count)
        count = 1
        prev = i

res += prev + str(count)
print(res)

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += [5]

if 'Ivan' in students:
    print(students)
