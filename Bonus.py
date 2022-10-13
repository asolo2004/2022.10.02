s = [int(x) for x in input('Введите целые элементы массива через пробел: ').split()]
delta = int(input('Введите delta: '))
mins = 10**10
k = 0
for i in s:
    if i < mins:
        mins = i
delta += mins
for i in s:
    if i >= delta:
        k += 1
print(k)
