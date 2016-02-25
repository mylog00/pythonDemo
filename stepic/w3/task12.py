keys = input()
values = input()

coded = input()
decoded = input()
vers_map = {}
revers_map = {}

coded2 = ''
decoded2 = ''
for i in range(len(keys)):
    vers_map[keys[i]] = values[i]
    revers_map[values[i]] = keys[i]
for i in range(len(coded)):
    coded2 += vers_map.get(coded[i])
for i in range(len(decoded)):
    decoded2 += revers_map.get(decoded[i])
print(coded2)
print(decoded2)
