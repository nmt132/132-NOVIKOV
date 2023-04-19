with open('c.txt') as f: #открытие файла
    n= [x for x in f] #создание списка значенний
    n.pop(0) #удаление первого элемента списка
   
    sp=[] #создание пустого списка
    for i in n: #цикл перебора всех значений списка
        sp.append(list(map(int,i.split())))
    k=[]#создание пустого списка
    ind=[]#создание пустого списка
    for i in range(len(sp)):
        if sp[i][1]%36==0:
            k.append(sp[i][1]//36)
        else: k.append((sp[i][1]//36)+1)
    for i in range(len(sp)):
        ind.append(sp[i][0])
    sp=list(zip(ind,k))#объединение двух списков в один
    costs=[]#создание пустого списка
    for i in range (549720,549728,1):
        pos= sp[i][0]
        cost=0#обнуление переменной
        for x in sp:
            cost=cost+abs(pos-x[0])*x[1]
        costs.append(cost)
        print(i,sp[i][0],cost)#вывод на печать номера пункта,километра, стоимости

       
