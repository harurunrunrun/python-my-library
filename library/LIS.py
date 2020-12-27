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
