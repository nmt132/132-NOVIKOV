with open('a.txt') as f:
    n= [x for x in f]
    n.pop(0)
   
    sp=[]
    for i in n:
        sp.append(list(map(int,i.split())))
    k=[]
    ind=[]
    for i in range(len(sp)):
        if sp[i][1]%36==0:
            k.append(sp[i][1]//36)
        else: k.append((sp[i][1]//36)+1)
    for i in range(len(sp)):
        ind.append(sp[i][0])
    sp=list(zip(ind,k))
    print(sp)
