from math import*
a = 11
n=20
S=0
pw=0
for item in range (a, n+1):
    divide = (item/10)
    change_sign=divide*pow(-1, pw)
    pw+=1
    S+=change_sign
    print("Change=", change_sign)
print("Total=", S)