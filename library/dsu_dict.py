import collections
class dsu_dict:
  def __init__(self):
    self.parents=collections.defaultdict(lambda:-1)
    return
  
  def merge(self,x,y):
    x=self.leader(x)
    y=self.leader(y)
    if x==y:
      return
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x
    return
    
  def size(self,x):
    return -self.parents[self.leader(x)]
    
  def same(self,x,y):
    return self.leader(x)==self.leader(y)
  
  def leader(self,x):
    if self.parents[x]<0:
      return x
    self.parents[x]=self.leader(self.parents[x])
    return self.parents[x]
  
  def groups(self):
    res=collections.defaultdict(list)
    for i in self.parents.keys():
      res[self.leader(i)].append(i)
    return list(res.values())
