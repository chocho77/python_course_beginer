import math

a = 0.1

while a < 0.9:
    num1 = math.sqrt(1 - a)
    num2 = 1 / num1
    a += 0.1
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")




