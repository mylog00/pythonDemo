# a, b = (int(i) for i in input().split())

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

a = 1
b = 3
c = 2
d = 4
print("\t", end='')
for i in range(c, d+1):
    print(str(i) + "\t", end='')
print("")
for i in range(a, b+1):
    print(str(i) + "\t", end='')
    for j in range(c, d+1):
        print(str(i * j) + "\t", end='')
    print("")
