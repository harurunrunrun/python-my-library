def next_permutation(d):
  for i in range(len(d)-2,-1,-1):
    if d[i]<d[i+1]:
      for j in range(len(d)-1,i,-1):
        if d[i]<d[j]:
          d[i],d[j]=d[j],d[i]
          l=i+1
          r=len(d)-1
          while l<r:
            d[l],d[r]=d[r],d[l]
            l+=1
            r-=1
          return True
  return False
