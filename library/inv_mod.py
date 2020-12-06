#乗法逆元を返します。Nが素数ではないときも有効です。
def ext_gcd(a,b):
  if b>a:
    a,b=b,a
  a0,x0,y0=a,1,0
  a1,x1,y1=b,0,1
  while a1!=0:
    q=a0//a1
    a2,x2,y2=a0-q*a1,x0-q*x1,y0-q*y1
    a0,x0,y0=a1,x1,y1
    a1,x1,y1=a2,x2,y2
  return a0,x0,y0

def inv_mod(a,N):
  d,x,y=ext_gcd(a,N)
  if d!=1:
    raise Exception("乗法逆数が存在しません。")
  return y%N

