from random import random, randint
k = int(input('Введите размерность массива: '))
s = []
mmax = -101
c = -1
for i in range(0, k):
    s.append(random()+randint(-100, 100))
    print(s[i], end=' ')
    if s[i] > mmax:
        mmax = s[i]
        c = i
print()
if c != -1 and c != k:
    for i in range(c+1, k):
        s[i] = 0
for i in range(0, k):
    print(s[i], end=' ')
