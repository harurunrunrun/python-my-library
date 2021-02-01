def zaatu(l):
  s=sorted(list(set(l)))#O(NlogN)
  c={}
  for i in range(len(s)):#O(N)
    c[s[i]]=i
  ret=[]
  for i in l:#O(N)
    ret.append(c[i])
  return ret
  
