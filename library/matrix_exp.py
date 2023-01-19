def matrix_mul(A,B,mod):
  C=[[0]*len(B[0])for _ in[0]*len(A)]
  for i in range(len(A)):
    for k in range(len(B)):
      for j in range(len(B[0])):
        C[i][j]=(C[i][j]+A[i][k]*B[k][j])%mod
  return C

def matrix_exp(X,n,mod):
  Y=[[0]*len(X)for _ in[0]*len(X)]
  for i in range(len(X)):
    Y[i][i]=1
  while n>0:
    if n&1:
      Y=matrix_mul(Y,X,mod)
    X=matrix_mul(X,X,mod)
    n>>=1
  return Y

def calculate_nth(mod,n,A0=0,A1=1,A=[[1,1],[1,0]]):
  # ex:fibonacci
  A=matrix_exp(A,n,mod)
  res=matrix_mul(A,[[A1],[A0]],mod)
  return res[1][0]

