#Cтандартний алгоритм, що поміняє місцями значення аргументів
a = int(input("Введіть перше значення:"))
b = int(input("Введіть друге значення:"))
Swap = a
a = b
b = Swap
print("Перше значення після змін: " + str(a))
print("Друге значення після змін: " + str(b))
#Особливість мови Python, що поміняє місцями значення аргументів
a, b =b, a
print("Перше значення після змін за допомогою (a, b =b, a): " + str(a))
print("Друге значення після змін за допомогою (a, b =b, a): " + str(b))
