#ACL
def is_prime(n):
  assert(0<=n<=4294967296)
  if n in [2,7,61]:
    return True
  if n<=1 or n%2==0:
    return False
  d=n-1
  while d%2==0:
    d//=2
  for a in [2,7,61]:
    t=d
    y=pow(a,t,n)
    while t!=n-1 and y not in [1,n-1]:
      y=y*y%n
      t<<=1
    if y!=n-1 and t%2==0:
      return False
  return True
  
