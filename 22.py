from math import *
x = 2
multiple=1
sum=0+1+x
n=2
for i in range (1, n+1):
    multiple *= 1/(i)
    print(multiple)
    sum += (pow(x, i)/multiple)
print("Factorial total=", sum)