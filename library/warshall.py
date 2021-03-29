#d[MAX_V][MAX_V]
#d[u][v]:edge e=(u,v)のコスト 存在しない場合はINF 但し、d[i][i]=0
#V:頂点数
def warshall(d:list,V:int):
  for k in range(V):
    for i in range(V):
      for j in range(V):
        if d[i][j]!=float("inf") and d[j][i]!=float("inf"):
          d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  return d
