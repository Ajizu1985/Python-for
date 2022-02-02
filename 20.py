from math import *
a = 3.3
sum=1
sum1=0
n=4
for i in range (1, n+1):
    multiple = i
    print(multiple)
    sum *= multiple
    sum1 += sum
print("Factorial=", sum1)