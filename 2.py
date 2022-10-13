from random import randint
k1 = int(input('Введите размерность 1 массива: '))
k2 = int(input('Введите размерность 2 массива: '))
s1 = []
s2 = []
k = False
for i in range(0, k1):
    s1.append(randint(0, 20))
    print(s1[i], end=' ')
print()
for i in range(0, k2):
    s2.append(randint(0, 20))
    print(s2[i], end=' ')
print()
for i in range(0, k1):
    if s1[i] in s2:
        print(s1[i], end=' ')
        s2.remove(s1[i])
        k = True
if not k:
    print('Нет общих элементов')
