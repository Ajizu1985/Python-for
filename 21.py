from math import *
a = 3.3
multiple=1
sum=1
n=5
for i in range (1, n+1):
    multiple *= 1/(i)
    print(multiple)
    sum += multiple
print("Factorial total=", sum)