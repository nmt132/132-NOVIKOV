def a():
    chisla='0123456789'
    chisla_spisok=list(chisla)
    print(chisla_spisok)
    haming='0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    haming_spisok=haming.split()
    print(haming_spisok)
    def distance(x,y):
        k=7
        for i in range(7):
            if x%10==y%10:
                k=k-1
            x=x//10
            y=y//10
        return k
    cod=int(input("код= "))
    min=distance(cod,int(haming_spisok[0]))
    imin=0
    for i in range(1,9):
        D=distance(cod,int(haming_spisok[i]))
        if D<min:
            min=D
            imin=i
    print(min)     
    if min==0:
        print(f"код верный: символ {chisla_spisok[imin]}")
    elif min==1:
        print(f"код исправлен: символ {chisla_spisok[imin]}")
    else:
        print("код неверный")
def b():
    a = "abwgdevijklmnoprstufhcqx"
    abc = list(a)
    print(abc)
    b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
    abcm=b.split()
    print(abcm)
    abcm=b.split()
    text=input("Введите текст на английском: ")
    indm=""
    for i in range (len(text)):
        ind = abc.index(text[i])
        indm=indm + abcm[ind] 
    print(f"{indm}")
def c():
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
def d():
    p = int(input("vvedite p (2<p<=10):"))
    x,y = int(1),int(1)
    for x in range (1,p):
        a=[]
        for y in range (1,p):
            z = (x*y//p)*10 + (x*y)% p
            a.append(z)
        print(a)
def h():
    print("Вdедите Число")
    N10 = int(input())
    print("Куда")
    p = int(input())
    k = 1
    Np = 0
    flag = True
    while flag == True:
        Np = Np + (N10 %p)*k
        k=k*10
        N10 = N10 // p
        if N10 == 0: 
            flag = False
    print(Np)
    
print ("выберите программу")
print ("код хемминга - 1")
print ("морзе - 2")
print ("перевод из n-ной в десятичную - 3")
print ("таблица умножения - 4")
print ("перевод из десятичной в n-ную - 5")
e  = int(input())
if e ==1:
    a()
elif e==2:
    b()
elif e== 3:
    c()
elif e== 4:
    d()
elif e == 5:
    h()
else:
    print("ошибка")
