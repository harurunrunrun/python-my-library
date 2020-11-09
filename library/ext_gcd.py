def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)

def ext_gcd(a,b):
  change=False
  if b>a:
    a,b=b,a
    change=True
  a0,x0,y0=a,1,0
  a1,x1,y1=b,0,1
  while a1!=0:
    q=a0//a1
    a2,x2,y2=a0-q*a1,x0-q*x1,y0-q*y1
    a0,x0,y0=a1,x1,y1
    a1,x1,y1=a2,x2,y2
  t=gcd(a,b)
  f1,f2=False,False
  if a*x0+b*y0==t:
    f1=True
  if a*y0+b*x0==t:
    f2=True
  if f1 and f2:
    x0,y0=min(x0,y0),max(x0,y0)
  elif f1 and change:
    x0,y0=y0,x0
  elif f2 and not change:
    x0,y0=y0,x0
  return a0,x0,y0  
  """
  if you not need a0, plz erase.
  if (x0,y0) is not one, return is min(|x|+|y|).(and more, if min is 2 return x<=y) 
  """
