for i in range(2023,10**10,2023):
    n=str(i)
    if n[0]=='1' and n[2:6]=='2139' and n[-1]=='4':
        print(i,i//2023)
