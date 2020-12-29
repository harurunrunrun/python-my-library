#降順プライオリティキュー heapqを使用したほう こっちのほうが安全 heapq に-1をその場で掛けたほうよりかなり遅い
from heapq import heapify,heappush,heappop
class maxheapq():
  def __init__(self,d):
    self.heap=[]
    for i in d:
      self.heap.append(-i)
    heapify(self.heap)
    return

  def mpush(self,x):
    heappush(self.heap,-x)
    return
    
  def mpop(self):
    return -1*(heappop(self.heap))
    
  def empty(self):
    return not bool(self.heap)
    
  def debug(self):
    return self.heap
