from heapq import heapify,heappop,heappush
INF=1000000000000000000
V=0
G=[[] for _ in [0]*100000]
d=[INF]*100000

def dijkstra(s):
  que=[]
  heapify(que)
  d[s]=0
  heappush(que,[0,s])
  while que:
    p=heappop(que)
    v=p[1]
    if d[v]<p[0]:
      continue
    for i in range(len(G[v])):
      e=G[v][i]
      if d[e[0]]>d[v]+e[1]:
        d[e[0]]=d[v]+e[1]
        heappush(que,[d[e[0]],e[0]])
"""
G[from].append([to,value])で追加
"""
