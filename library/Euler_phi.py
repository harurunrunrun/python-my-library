def Euler_phi(n):
  assert n>0,"not defiend"
  if n==1:
    return 1
  E_i=2
  E_ans=1
  while E_i*E_i<n:
    E_cnt=0
    while n%E_i==0:
      n//=E_i
      E_cnt+=1
    if E_cnt!=0:
      E_ans*=pow(E_i,E_cnt-1)*(E_i-1)
    E_i+=1
  if n!=1:
    E_ans*=n-1
  return E_ans
