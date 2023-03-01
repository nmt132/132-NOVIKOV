for i in range(2023,10**10,2023):
    n=str(i)
    if n[0]=='1' and n[2:6]=='2139' and n[-1]=='4':
        print(i,i//2023)
for i in range(13450608,10**20):
    n=str(i)
    if n[0]=='1' and n[1:5]=='2345' and n[8]=='8'and n[6] =='6':
        if i%17==0:
            print(i,i//17)
