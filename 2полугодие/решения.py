def f8():
  count=0
  for a in range (1,8):
      for b in range (8):
          for c in range (8):
              for d in range (8):
                  for e in range (8):
                      s=str(a)+str(b)+str(c)+str(d)+str(e)
                      if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                          count+=1
                      if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0:
                          count+=1
                      if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                          count+=1
print(count)
def f81():
  from itertools import product
  nums=product('01234567',repeat=5)
  k=0
  n='16 36 56 76 61 63 65 67'
  nn=n.split()
  for n in nums:
      numb=''.join(n)
      sp=[]
      if numb.count('6')==1 and numb[0]!='0':
          for x in nn:
              if x in numb:
                  sp.append(x)
          if not sp: 
              k+=1
  print(k)
def f12:
  for i in range (2,1000):
    k=0
    for n in range(2,i-1):
        if i%n == 0:
            k=1
    if k ==0:
        d= (i-117)%4
        if d==0:
            if i>121:
                f=(i-117)/4
                print(f)
def f15:
  for a in range(1000):
    if all((x%2==0)<=(x%3!=0) or (x+a>=100) for x in range(1,100)):
        print(a)
        break
def f23:
  from itertools import product
  def f(x,y,z):
      k= 0
      for i in range(2,z):
          b=product('12',repeat=i)
          for n in b:
              if(x==10 and n.count('2')>1):
                continue
              a=x
              for l in n:
                  if l=='1':
                      a+=1
                  else :
                      a*=2
                  if a==17:
                      break
              if a==y:
                 k+=1

      return(k)  
  print(f(1,10,10))
  print(f(10,35,25))

def f223:
  def f(x,y):
    if x>y or x==17:
        return 0

    elif x==y: return 1
    return f(x+1,y) + f(x*2,y)
  print(f(1,10)*f(10,35))

def f161:
  a = 1
  b = 1
  for i in range (1,2024):
      a=a*i
  for i in range (1,2021):
      b=b*i
  print(a/b)
 def162:
  import sys 
  sys.setrecursionlimit(50000)
  def f(n):
      if n==1: return f(n)-1
      elif n>1: return n*f(n-1)
    
  print(f(2023)/f(2020))
def f17:
 
with open('17.txt') as f:
    a=[int(x)for x in f]
    c=list(map(abs,a))
    count=0
    sp=[]
    for i in range(len(a)-1):
        if abs(a[i])%10==4:
            sp.append(a[i])
    maxi=max(sp)**2
    sp2=[]
    for i in range(len(c)-1):
        if ((c[i]%10==4 and c[i+1]%10!=4 ) or (c[i]%10!=4 and c[i+1]%10==4)) and (c[i]**2+c[i+1]**2)>=maxi:
            count+=1
            sp2.append(c[i]**2+c[i+1]**2)
    print(count)
    print(min(sp2))
