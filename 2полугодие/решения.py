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

