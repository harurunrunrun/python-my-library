def lcss(S,T):
  dp=[[0]*(len(T)+1)for _ in[0]*(len(S)+1)]
  ret=0
  for i in range(len(S)):
    for j in range(len(T)):
      if S[i]==T[j]:
        if i<0 or j<1:
          dp[i][j]=1
        else:
          dp[i][j]=dp[i-1][j-1]+1
        ret=max(ret,dp[i][j])
  return ret
