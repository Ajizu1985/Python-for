from math import *
a = 3.3
sum=0
n=4
for i in range (0, n+1):
    powr = pow(-a, i)
    print(powr)
    sum += powr
print("Total=", sum)
