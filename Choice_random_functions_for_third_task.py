#Ця програма генерує 5 випадкових унікальних чисел для вибору функцій які будуть реалізовані у 3 завданні
from numpy.random import randint
listFunction = [randint(1, 16) for i in range(5)]
i = 0
j = 0
while i != len(listFunction):
    while j != i:
        if listFunction[i] == listFunction[j]:
            listFunction[j] = randint(1, 16)
        j += 1
    j = 0
    i += 1
print(listFunction)