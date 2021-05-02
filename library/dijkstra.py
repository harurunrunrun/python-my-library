class dijkstra:
  def __init__(self,V):
    self.INF=float("inf")
    self.G=[[] for _ in [0]*V]
    self.V=V
    return
  
  def add1(self,s,t,v):
    self.G[s].append([t,v])
    return
  
  def add2(self,s,t,v):
    self.G[s].append([t,v])
    self.G[t].append([s,v])
    return

  def run(self,s):
    from heapq import heapify,heappop,heappush
    ret=[self.INF]*self.V
    que=[]
    heapify(que)
    ret[s]=0
    heappush(que,(0,s))
    while que:
      p=heappop(que)
      v=p[1]
      if ret[v]<p[0]:
        continue
      for i in range(len(self.G[v])):
        e=self.G[v][i]   
        if ret[e[0]]>ret[v]+e[1]:
          ret[e[0]]=ret[v]+e[1]
          heappush(que,(ret[e[0]],e[0]))
    return ret

