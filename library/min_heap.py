class min_heap():
  def __init__(self,d):
    
    if not isinstance(d,list):
      raise ValueError(f"1st argument must be list, not {str(type(d)).split()[-1][1:4]}.")
    
    self.e=1000000001         #単位元:これを上回るときは変える
    self.heap=[self.e]*500000  #heap:これ以上必要なときは増やす
    self.clock=1               #偏らないようにするためのもの(仮)
    
    for i in d:
      self.push(i)
    return
    
  def push(self,x):
    i=0
    idx=x
    while self.heap[i]!=self.e:
      if self.heap[i]>idx:
        t=idx
        idx=self.heap[i]
        self.heap[i]=t      
      if self.heap[2*i+1]==self.e:
        i=2*i+1
      elif self.heap[2*i+2]==self.e:
        i=2*i+2
      else:
        if self.clock>0:
          i=2*i+1
        else:
          i=2*i+2
        self.clock*=-1
    
    self.heap[i]=idx
    return
  
  def pop(self):
    ret=self.heap[0]
    if ret==self.e:
      raise Exception("heap is empty.")
      return
    i=0
    
    while self.heap[i]!=self.e:
      left=2*i+1
      right=2*i+2
    
      left_bool=self.heap[left]==self.e
      right_bool=self.heap[right]==self.e
    
      if left_bool and right_bool:
        self.heap[i]=self.e
        return ret
    
      if right_bool:
        self.heap[i]=self.heap[left]
        i=left
        continue
      if left_bool:
        self.heap[i]=self.heap[right]
        i=right
        continue
    
      if self.heap[left]<self.heap[right]:
        self.heap[i]=self.heap[left]
        i=left
      else:
        self.heap[i]=self.heap[right]
        i=right
    return ret
    
  def empty(self):
    if self.heap[0]==self.e:
      return True
      #空ならTrue
    return False
  
  def debug(self):
    return self.heap
    
