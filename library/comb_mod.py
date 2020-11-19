def comb_mod(n,r,mod):
  if n-r<r:
    r=n-r
  N=n
  R=r
  u=1
  d=1
  for i in range(r):
    u*=N
    u%=mod
    N-=1
    d*=R
    d%=mod
    R-=1
  return u*pow(d,mod-2,mod)%mod
