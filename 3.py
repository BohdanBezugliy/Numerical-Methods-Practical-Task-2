import math

x = float(input("x = "))
xRad = x * math.pi/180

first_res = math.sqrt(math.cos(abs(xRad)))
first_res -= (((math.cos(2 * xRad) ** 2) + (math.sin(3 * xRad) ** 2)) / (x * (x - 1) * (x + 2))) * (math.exp(1 / x))
first_res += 2 * math.log(x * x + 2)
print("Результат першої функції: " + str(first_res))

second_res = 0
second_res += math.sqrt(abs(math.log((x ** 2) + 1)))
second_res += (2*(x-5))/(x*(x+1))
second_res -= x * math.exp(1/x)
print("Результат другої функції: " + str(second_res))

third_res = 0
third_res += math.sqrt(1 + abs(math.cos(xRad)))
third_res += (math.cos(2 * xRad) - (math.sin(3*xRad) ** 2))/(x * ((2 * x) - 1) * (x + 2))
third_res += math.exp(1 / (2 * x)) * math.log((x ** 2) + 1)
print("Результат третьої функції: " + str(third_res))

forth_res = 0
forth_res += math.sqrt(3 + abs(math.log(2 * (x ** 2) + 1)))
forth_res += (2 + (x - 5)) / (x * (x + 1) * (3 * (math.cos(4 * xRad) ** 3) + (math.sin(3 * xRad) ** 2)))
forth_res += 2 * x * math.exp(1 / (3 * x))
print("Результат четвертої функції: " + str(forth_res))


fifth_res = 0
fifth_res += math.sqrt(((math.cos(3+xRad) ** 2) - 4 * (math.sin(3 * xRad) ** 2)) / (x + (x + 1) * abs(x - 2)) + 1)
fifth_res += 3 * math.log(abs(4*x-1))
fifth_res += x - math.exp(1/x) + 4
print("Результат п'ятої функції: " + str(fifth_res))
