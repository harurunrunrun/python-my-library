class INPUT:
  def __init__(self):
    self.l=open(0).read().split()[::-1]
    self.length=len(self.l)
    return
  
  def stream(self,k,f=True):
    assert(-1<k)
    m=self.length
    if m==0 or m<k:
      raise Exception("too much requirement!")
    elif f:
      if k==0:
        self.length=0
        return list(map(int,self.l[::-1]))
      if k==1:
        self.length-=1
        return int(self.l.pop())
      ret=[]
      for _ in [0]*k:
        ret.append(int(self.l.pop()))
      self.length-=k
      return ret
    else:
      if k==0:
        self.length=0
        return self.l[::-1]
      if k==1:
        self.length-=1
        return self.l.pop()
      ret=[]
      for _ in [0]*k:
        ret.append(self.l.pop())
      self.length-=k
      return ret
pin=INPUT().stream
"""
pin(number,int[default:True])
"""
