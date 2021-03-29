def lcm(S,T):
  dp=[[0]*(len(T)+1)for _ in[0]*(len(S)+1)]
  for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
      if S[i-1]==T[j-1]:
        dp[i][j]=dp[i-1][j-1]+1
      else:
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
  length=dp[len(S)][len(T)]
  i=len(S)
  j=len(T)
  ans=""
  while length>0:
    if S[i-1]==T[j-1]:
      ans+=S[i-1]
      i-=1
      j-=1
      length-=1
    elif dp[i][j]==dp[i-1][j]:
      i-=1
    else:
      j-=1
  return ans[::-1]

