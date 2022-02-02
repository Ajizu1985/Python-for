from math import*
a = 1
n=5
S=0
for item in range (a, n+1, 2):
    S+=item
    powr = pow(S, 2)
    print("Item=", item)
print("Total=", powr)