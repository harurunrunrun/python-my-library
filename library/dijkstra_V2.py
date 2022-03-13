class dijkstra_V2:
  def __init__(self,V):
    self.INF=float("inf")
    self.cost=[[self.INF]*V for _ in [0]*V]
    self.V=V
    return

  def add1(self,s,t,v):
    self.cost[s][t]=v
    return

  def add2(self,s,t,v):
    self.cost[s][t]=v
    self.cost[t][s]=v
    return

  def run(self,s):
    ret=[self.INF]*self.V
    ret[s]=0
    used=[False]*self.V
    while 1:
      v=-1
      for u in range(self.V):
        if (not used[u]) and (v==-1 or ret[u]<ret[v]):
          v=u
      if v==-1:
        break
      used[v]=True
      for u in range(self.V):
        if ret[u]>ret[v]+self.cost[v][u]:
          ret[u]=ret[v]+self.cost[v][u]
    return ret
