def modify_list(l):
    a = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] //= 2
        else:
            a.append(l[i])
    for i in a:
        l.remove(i)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
