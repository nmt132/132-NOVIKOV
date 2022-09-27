p = int(input("vvedite p (2<p<=10):"))
x,y = int(1),int(1)

for x in range (1,p):
   a=[]
   for y in range (1,p):
      z = (x*y//p)*10 + (x*y)% p
      a.append(z)
   print(a)

