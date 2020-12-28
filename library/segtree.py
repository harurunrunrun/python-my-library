#atcoder library python master の写しです。
class SegTree():
  def __init__(self,op,e,v):
    self._op=op
    self._e=e
    
    if isinstance(v,int):
      v=[e]*v
    
    self._n=len(v)
    self._log=self.ceil2()
    self._size=1<<self._log
    self._d=[e]*(2*self._size)
    
    for i in range(self._n):
      self._d[self._size+i]=v[i]
    for i in range(self._size-1,0,-1):
      self._update(i)
    return
  
  def ceil2(self):
    x=0
    while (1<<x)<self._n:
      x+=1
    return x
    
  def set(self,p,x):
    p+=self._size
    self._d[p]=x
    for i in range(1,self._log+1):
      self._update(p>>i)
    return
    
  def get(self,p):
    return self._d[p+self._size]
    
  def prod(self,left,right):
    sml=self._e
    smr=self._e
    left+=self._size
    right+=self._size
    while left<right:
      if left&1:
        sml=self._op(sml,self._d[left])
        left+=1
      if right&1:
        right-=1
        smr=self._op(self._d[right],smr)
      left>>=1
      right>>=1
    return self._op(sml,smr)
    
  def all_prod(self):
    return self._d[1]
  
  #max_right min_left バグってしまった
  
  def _update(self,k):
    self._d[k]=self._op(self._d[2*k],self._d[2*k+1])
    return

  def _f(u,v):
    return u<v
