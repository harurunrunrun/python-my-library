class dsu:
  def __init__(self,n):
    assert n>0,"n must be Natural"
    self.n=n
    self.parents=[-1]*n
    return
  
  def find(self,x):
    assert x<self.n,"warning!! this is 0 index"
    if self.parents[x]<0:
      return x
    self.parents[x]=self.find(self.parents[x])
    return self.parents[x]
  
  def merge(self,x,y):
    assert x<self.n and y<self.n,"warning!! this is 0 index"
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x
    return
    
  def size(self,x):
    assert x<self.n,"warning!! this is 0 index"
    return -self.parents[self.find(x)]
    
  def same(self,x,y):
    assert x<self.n and y<self.n,"warning!! this is 0 index"
    return self.find(x)==self.find(y)
  
  def leader(self,x):
    assert x<self.n,"warning!! this is 0 index"
    if self.parents[x]<0:
      return x
    self.parents[x]=self.leader(self.parents[x])
    return self.parents[x]
  
  def groups(self):
    ld=[self.leader(i) for i in range(self.n)]
    res=[[] for _ in range(self.n)]
    for i in range(self.n):
      res[ld[i]].append(i)
    return list(filter(lambda a:a !=[],res))


#es[i]=[u,v,cost]
#V:頂点数
#E:辺数

def kruskal(es,V,E):
  es=sorted(es,key=lambda x:x[2])
  uf=dsu(V)
  ret=0
  for i in range(E):
    e=es[i]
    if not uf.same(e[0],e[1]):
      uf.merge(e[0],e[1])
      ret+=e[2]
  return ret
