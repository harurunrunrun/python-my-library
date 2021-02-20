def bell(start):
  d[start]=0
  for i in range(V):
    f=True
    for j in G:
      From,to,cost=j
      if d[to]>d[From]+cost:
        d[to]=d[From]+cost
        f=False
    if f:
      break
    if i==V-1:
      return False
  return True


V,E=map(int,input().split())
d=[float("inf")]*V
G=[]
for i in range(E):
  a,b,c=map(int,input().split())
  G.append([a,b,c])
  #G.append([b,a,c])#無向の場合のみ

#float("inf")が出力されるときに注意
