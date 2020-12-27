def LIS_dp(a):
  res=0
  dp=[0]*len(a)
  for i in range(len(a)):
    dp[i]=1
    for j in range(i):
      if a[j]<a[i]:
        dp[i]=max(dp[i],dp[j]+1)
    res=max(res,dp[i])
  return res
