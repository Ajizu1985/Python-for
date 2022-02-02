from math import*
a = 11
n=14
S=1
for item in range (a, n+1):
    divide = (item/10)
    S*=divide
    print("Add=", divide)
print("Total=", S)