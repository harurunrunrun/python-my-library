class dijkstra:
  def __init__(self):
    self.INF=float("inf")
    self.G=[[] for _ in [0]*100000]
    self.d=[self.INF]*100000
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
    que=[]
    heapify(que)
    self.d[s]=0
    heappush(que,[0,s])
    while que:
      p=heappop(que)
      v=p[1]
      if self.d[v]<p[0]:
        continue
      for i in range(len(self.G[v])):
        e=self.G[v][i]   
        if self.d[e[0]]>self.d[v]+e[1]:
          self.d[e[0]]=self.d[v]+e[1]
          heappush(que,[self.d[e[0]],e[0]])
    return self.d


