# 頂点0 から各頂点を1周してもどってくる最短コスト
def bitDP(N,G):
  # N : 頂点数
  # G : G[i][j] i->jへのコスト
  INF=10**18
  dp=[[INF]*N for _ in[0]*(1<<N)]
  dp[0][0]=0
  for S in range(1<<N):
    for v in range(N):
      for u in range(N):
        if (u==v) or (S and not (S>>u)&1):
          continue
        if (S>>v)&1==0:
          dp[S|(1<<v)][v]=min(dp[S|(1<<v)][v],dp[S][u]+G[u][v])
  if dp[-1][0]==INF:
    return -1
  return dp[-1][0]
  