class StaticRangeSum():
  def __init__(self,a):
    if type(a)!=list:
      raise ValueError(f"""argument must be list not {str(type(a)).split("'")[1]}.""")
    self._d=[0]
    self._n=len(a)
    for i in range(self._n):
      self._d.append(self._d[i]+a[i])
    return
  def rsum(self,l,r):
    assert(0<=l<self._n)
    assert(0<=r<self._n)
    #0-index sum([l,r])
    return self._d[r+1]-self._d[l]
