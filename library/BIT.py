class BIT():
  def __init__(self,a):
    self.n=len(a)
    self.bit=[0]*(self.n+1)
    for i,e in enumerate(a):
      self.add(i+1,e)
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
