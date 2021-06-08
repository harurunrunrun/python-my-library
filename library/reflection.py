#(xp1,yp1),(xp2,yp2)を通る直線を軸として、(xp,yp)と対称な点を求める
def reflection(xp1,yp1,xp2,yp2,xp,yp):
  assert((xp1,yp1)!=(xp2,yp2))
  if xp1==xp2:
    return (2*xp1-xp,yp)
  if yp1==yp2:
    return (xp,2*yp1-yp)
  xm=xp1-xp2
  ym=yp1-yp2
  if xm*yp==ym*(xp-xp1)+yp1:
    return (xp,yp)
  x=((xm**2-ym**2)*xp+2*(ym**2)*xp1+2*xm*ym*(yp-yp1))/(xm**2+ym**2)
  y=((ym**2-xm**2)*yp+2*xm*ym*(xp-xp1)+2*(xm**2)*yp1)/(xm**2+ym**2)
  return (x,y)
