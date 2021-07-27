from collections import deque
class LCA:
  def __init__(self,N:int,G:list,root:int=0):
    self.LV=(N-1).bit_length()
    self.depth=[0]*N
    self.parent=[-1]*N
    self.children=[[]for _ in[0]*N]
    dq=deque()
    dq.append(root)
    check=[True]*N
    while dq:
      q=dq.pop()
      check[q]=False
      for i in G[q]:
        if check[i]:
          self.depth[i]=self.depth[q]+1
          dq.append(i)
          self.parent[i]=q
          self.children[q].append(i)
    self.kprv=[self.parent]
    S=self.parent
    for k in range(self.LV):
      T=[0]*N
      for i in range(N):
        if S[i] is None:
          continue
        T[i]=S[S[i]]
      self.kprv.append(T)
      S=T
    return
  
  def lca(self,u,v):
    dd=self.depth[v]-self.depth[u]
    if dd<0:
      u,v=v,u
      dd=-dd
    for k in range(self.LV+1):
      if dd&1:
        v=self.kprv[k][v]
      dd>>=1
    if u==v:
      return u
    for k in range(self.LV-1,-1,-1):
      pu=self.kprv[k][u]
      pv=self.kprv[k][v]
      if pu!=pv:
        u=pu
        v=pv
    return self.kprv[0][u]