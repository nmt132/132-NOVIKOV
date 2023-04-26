from itertools import product
maxi = 0
s=0
b=0
sp=[[0,712,673,1075,875,1622,423],
[712,0,1385,1800,1577,2348,1128],
[673,1385,0,1499,239,2046,244],
[1075,1800,1499,0,1287,551,1266],
[875,1577,239,1287,0,1835,442],
[1622,2348,2046,551,1835,0,1813],
[423,1128,244,1266,442,1813,0]]
a=product('0123456',repeat=7)
alp='0123456'
for i in a:
    s=0
    if all(i.count(x)==1 for x in alp):
        for j in range(len (i) -1):
            s+=sp[int(i[j])][int(i[j+1])]
            if s>maxi:
                maxi=s 
                b= i[:]
print(maxi,''.join(b))
