import math
x = float(input("x = "))
xRad = x * math.pi/180
first_res = math.sqrt(math.cos(abs(xRad)))
first_res -= (((math.cos(2 * xRad) ** 2) + (math.sin(3 * xRad) ** 2)) / (x * (x - 1) * (x + 2))) * (math.exp(1 / x))
first_res += 2 * math.log(x * x + 2)
print("Результат першої функції: " + str(first_res))
