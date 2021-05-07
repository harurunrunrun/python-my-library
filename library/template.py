##template harurun##
from collections import Counter,deque
from itertools import permutations
from math import sqrt,isqrt,pi,comb
from sys import setrecursionlimit
setrecursionlimit(10000000)
from heapq import heapify,heappop,heappush
######ベルマンフォード#####
class bell:
  def __init__(self,V):
    self._d=[float("inf")]*V
    self._G=[]
    self._V=V
    return
  
  def run(self,start):
    self._d[start]=0
    for i in range(self._V):
      f=True
      for j in self._G:
        From,to,cost=j
        if d[to]>d[From]+cost:
          d[to]=d[From]+cost
          f=False
      if f:
        break
      if i==self._V-1:
        return False
    return True

  def add1(s,t,c):
    self._G.append([s,t,c])
    return
  
  def add2(s,t,c):
    self._G.append([s,t,c])
    self._G.append([t,s,c])
    return

###フェニック木###
class BIT():
  def __init__(self,a):
    self.n=len(a)
    self.bit=[0]*(self.n+1)
    for i,e in enumerate(a):
      self.add(i+1,e)
    return
  
  def sum(self,i):
    s=0
    while i>0:
      s+=self.bit[i]
      i-=i&-i
    return s
  
  def add(self,i,x):
    while i<=self.n:
      self.bit[i]+=x
      i+=i&-i
    return

###ダイクストラ###
class dijkstra:
  def __init__(self,V):
    self.INF=float("inf")
    self.G=[[] for _ in [0]*V]
    self.V=V
    return
  
  def add1(self,s,t,v):
    self.G[s].append([t,v])
    return
  
  def add2(self,s,t,v):
    self.G[s].append([t,v])
    self.G[t].append([s,v])
    return

  def run(self,s):
    from heapq import heapify,heappop,heappush
    ret=[self.INF]*self.V
    que=[]
    heapify(que)
    ret[s]=0
    heappush(que,(0,s))
    while que:
      p=heappop(que)
      v=p[1]
      if ret[v]<p[0]:
        continue
      for i in range(len(self.G[v])):
        e=self.G[v][i]   
        if ret[e[0]]>ret[v]+e[1]:
          ret[e[0]]=ret[v]+e[1]
          heappush(que,(ret[e[0]],e[0]))
    return ret

###Union Find###
class dsu:
  def __init__(self,n):
    assert n>0,"n must be Natural"
    self.n=n
    self.parents=[-1]*n
    return
  
  def find(self,x):
    assert x<self.n,"warning!! this is 0 index"
    if self.parents[x]<0:
      return x
    self.parents[x]=self.find(self.parents[x])
    return self.parents[x]
  
  def merge(self,x,y):
    assert x<self.n and y<self.n,"warning!! this is 0 index"
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x
    return
    
  def size(self,x):
    assert x<self.n,"warning!! this is 0 index"
    return -self.parents[self.find(x)]
    
  def same(self,x,y):
    assert x<self.n and y<self.n,"warning!! this is 0 index"
    return self.find(x)==self.find(y)
  
  def leader(self,x):
    assert x<self.n,"warning!! this is 0 index"
    if self.parents[x]<0:
      return x
    self.parents[x]=self.leader(self.parents[x])
    return self.parents[x]
  
  def groups(self):
    ld=[self.leader(i) for i in range(self.n)]
    res=[[] for _ in range(self.n)]
    for i in range(self.n):
      res[ld[i]].append(i)
    return list(filter(lambda a:a !=[],res))

###クラスカル法###
class kruskal:
  def __init__(self,V,E):
    self._V=V
    self._E=E
    self._es=[]
    return
  
  def add(self,s,t,c):
    self._es.append([s,t,c])
    return
  
  def kruskal(es,V,E):
    self._es=sorted(self._es,key=lambda x:x[2])
    uf=dsu(V)
    ret=0
    for i in range(E):
      e=self._es[i]
      if not uf.same(e[0],e[1]):
        uf.merge(e[0],e[1])
        ret+=e[2]
    return ret

###max heapq###
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

###segment tree###
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
  
  def max_right(self,left,target):
    self.target=target
    if left==self._n:
      return self._n
    left+=self._size
    sm=self._e
    
    first=True
    while first or (left & -left)!=left:
      first=False
      while left%2==0:
        left>>=1
      if not self._f(self._op(sm,self._d[left])):
        while left<self._size:
          left*=2
          if self._f(self._op(sm,self._d[left])):
            sm=self._op(sm,self._d[left])
            left+=1
        return left-self._size
      sm=self._op(sm,self._d[left])
      left+=1
    return self._n
    
  def min_left(self,right,target):
    self.target=target
    if right==0:
      return 0
    
    right+=self._size
    sm=self._e
    
    first=True
    while first or (right&-right)!=right:
      first=False
      right-=1
      while right>1 and right%2:
        right>>=1
      if not self._f(self._op(self._d[right],sm)):
        while right<self._size:
          right=2*right+1
          if self._f(self._op(self._d[right],sm)):
            sm=self._op(self._d[right],sm)
            right-=1
        return right+1-self._size
      sm=self._op(self._d[right],sm)
    return 0
  
  def _update(self,k):
    self._d[k]=self._op(self._d[2*k],self._d[2*k+1])
    return

  def _f(self,u):
    return u<self.target

###ワーシャルフロイド###
class warshall:
  def __init__(self,V):
    self._V=V
    self._d=[[float("inf")]*V for _ in[0]*V]
    for i in range(V):
      self._d[i][i]=0
    return
  
  def add(self,u,v,c):
    if u==v:
      return
    self._d[u][v]=c
    return
  
  def run(self):
    for k in range(self._V):
      for i in range(self._V):
        for j in range(self._V):
          if self._d[i][j]!=float("inf") and self._d[j][i]!=float("inf"):
            self._d[i][j]=min(self._d[i][j],self._d[i][k]+self._d[k][j])
    return self._d

###関数テンプレート###
class tmp:
  ###最長増加部分列###
  def LIS(seq):
    #O(NlogN)
    from bisect import bisect_left
    ld=[seq[0]]
    for i in range(len(seq)):
      if seq[i]>ld[-1]:
        ld.append(seq[i])
      else:
        ld[bisect_left(ld,seq[i])]=seq[i]
    return len(ld)
  
  ###mod comb###
  def comb_mod(n,r,mod):
    if n-r<r:
      r=n-r
    N=n
    R=r
    u=1
    d=1
    for i in range(r):
      u*=N
      u%=mod
      N-=1
      d*=R
      d%=mod
      R-=1
    return u*pow(d,mod-2,mod)%mod

  def floor_sum(n,m,a,b):
    ans=0
    if a>=m:
      ans+=(n-1)*n*(a//m)//2
      a%=m
    if b>=m:
      ans+=n*(b//m)
      b%=m
  
    y_max=(a*n+b)//m
    x_max=y_max*m-b
  
    if y_max==0:
      return ans
    ans+=(n-(x_max+a-1)//a)*y_max
    ans+=floor_sum(y_max,a,m,(a-x_max%a)%a)
    return ans
  
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

  def inv_mod(self,a,N):
    d,x,y=self.ext_gcd(a,N)
    if d!=1:
      raise Exception("乗法逆数が存在しません。")
    return y%N

  #ACL
  def is_prime(n):
    assert(0<=n<=4294967296)
    if n in [2,7,61]:
      return True
    if n<=1 or n%2==0:
      return False
    d=n-1
    while d%2==0:
      d//=2
    for a in [2,7,61]:
      t=d
      y=pow(a,t,n)
      while t!=n-1 and y not in [1,n-1]:
        y=y*y%n
        t<<=1
      if y!=n-1 and t%2==0:
        return False
    return True
  
  ###longest common subsequence###最長共通部分列
  def lcs(S,T):
    dp=[[0]*(len(T)+1)for _ in[0]*(len(S)+1)]
    for i in range(1,len(S)+1):
      for j in range(1,len(T)+1):
        if S[i-1]==T[j-1]:
          dp[i][j]=dp[i-1][j-1]+1
        else:
          dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    length=dp[len(S)][len(T)]
    i=len(S)
    j=len(T)
    ans=""
    while length>0:
      if S[i-1]==T[j-1]:
        ans+=S[i-1]
        i-=1
        j-=1
        length-=1
      elif dp[i][j]==dp[i-1][j]:
        i-=1
      else:
        j-=1
    return ans[::-1]
  
  ###longest common substring###最長共通部分文字列(連続)
  #未verify
  def lcss(S,T):
    dp=[[0]*(len(T)+1)for _ in[0]*(len(S)+1)]
    ret=0
    for i in range(len(S)):
      for j in range(len(T)):
        if S[i]==T[j]:
          if i<0 or j<1:
            dp[i][j]=1
          else:
            dp[i][j]=dp[i-1][j-1]+1
          ret=max(ret,dp[i][j])
    return ret

  #エラトステネスの篩 n以下の素数の個数
  def sieve(n):
    #assert(1<n<10000000)
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
  
  ###転倒数###
  def tentou(a):
    l=[]#a:list
    for i in a:
      l.append(i)
    n=len(l)
    min_l=min(l)
    if min_l<1:
      for i in range(n):
        l[i]+=abs(min_l)+1
    ft=BIT(l)
    ans=0
    for i in range(n):
      ans+=i-ft.sum(l[i])
      ft.add(l[i],1)
    return ans
  
  ###1次元座圧###
  def zaatu(l):
    s=sorted(list(set(l)))#O(NlogN)
    c={}
    for i in range(len(s)):#O(N)
      c[s[i]]=i
    ret=[]
    for i in l:#O(N)
      ret.append(c[i])
    return ret

###入力class###
class INPUT:
  def __init__(self):
    self._l=open(0).read().split()
    self._length=len(self._l)
    self._index=0
    return

  def stream(self,k=1,f=int,f2=False):
    assert(-1<k)
    if self._length==self._index or self._length-self._index<k:
      raise Exception("There is no input!")
    elif f!=str:
      if k==0:
        ret=list(map(f,self._l[self._index:]))
        self._index=self._length
        return ret
      if k==1 and not f2:
        ret=f(self._l[self._index])
        self._index+=1
        return ret
      if k==1 and f2:
        ret=[f(self._l[self._index])]
        self._index+=1
        return ret
      ret=[]
      for _ in [0]*k:
        ret.append(f(self._l[self._index]))
        self._index+=1
      return ret
    else:
      if k==0:
        ret=list(self._l[self._index:])
        self._index=self._length
        return ret
      if k==1 and not f2:
        ret=self._l[self._index]
        self._index+=1
        return ret
      if k==1 and f2:
        ret=[self._l[self._index]]
        self._index+=1
        return ret
      ret=[]
      for _ in [0]*k:
        ret.append(self._l[self._index])
        self._index+=1
      return ret
pin=INPUT().stream

"""
pin(number[default:1],f[default:int],f2[default:False])
if number==0 -> return left all
listを変数で受け取るとき、必ずlistをTrueにすること。
"""
