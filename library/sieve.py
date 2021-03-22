#エラトステネスの篩 n以下の素数の個数
def sieve(n):
  assert(1<n<10000000)
  b=[True]*n
  b[0]=False
  ret=[]
  cnt=0
  for i in range(1,n):
    if b[i]:
      cnt+=1
      ret.append(i+1)
      for j in range(2*i+1,n,i+1):
        b[j]=False
  #return ret
  return cnt


