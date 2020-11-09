def comb_mod(N,R,mod):
  g1=[1,1]
  g2=[1,1]
  inverse=[0,1]
  for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)
  if R<0 or R>N:
    return 0
  R=min(R,N-R)
  ans=g1[N]*g2[R]*g2[N-R]%mod
  return ans
