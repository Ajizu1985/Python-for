from math import*
a = int(input("Pls enter any number = "))
n = int(input("Pls enter power level = "))
sum = 1
if n > 0:
    for i in range (1, n):
        sum *= a
print(sum)