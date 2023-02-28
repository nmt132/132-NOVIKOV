with open('24.txt') as f:
    cnt = 0
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    print(s)
    for i in s:
        if i =='*':
            cnt+=1
            hmax=max(hmax,cnt)
        else:
            cnt=0
    print(hmax)
