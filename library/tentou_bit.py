class BIT():
  def __init__(self,a):
    self.n=len(a)
    self.bit=[0]*(self.n+1)
    return
  
  def sum(self,i):
    s=0
    while i>0:
      s+=self.bit[i]
      i-=i&-i
    return s
  
  def add(self,i,x):
    while i<=self.n:
      self.bit[i]+=x
      i+=i&-i
    return

def tentou(a):
  l=[]#a:list
  for i in a:
    l.append(i)
  n=len(l)
  min_l=min(l)
  if min_l<1:
    for i in range(n):
      l[i]+=abs(min_l)+1
  ft=BIT(l)
  ans=0
  for i in range(n):
    ans+=i-ft.sum(l[i])
    ft.add(l[i],1)
  return ans
