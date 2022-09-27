print("p=")
a = int(input())
print("Np=")
b = int(input())
c = 1
d = 0
while b>0:
   d = d +(b%10)*c
   c = c*a
   b = b//10
print("N10=",d)
