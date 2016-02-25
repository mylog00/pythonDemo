file_path = 'task15.txt'
classes = list()
for i in range(11):
    classes.append([])
with open(file_path, 'r') as fr:
    for string in fr:
        strings = string.split('\t')
        num = int(strings[0]) - 1
        value = int(strings[2])
        classes[num].append(value)
counter = 1
for mas in classes:
    print(counter, end=' ')
    counter += 1
    if len(mas) <= 0:
        print('-')
    else:
        print(sum(mas) / len(mas))
