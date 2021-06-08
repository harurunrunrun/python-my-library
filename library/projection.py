#(xp1,yp1),(xp2,yp2)を通る直線に、(xp,yp)から垂線を下ろしたときの交点の座標を求める
def projection(xp1,yp1,xp2,yp2,xp,yp):
  assert((xp1,yp1)!=(xp2,yp2))
  if xp1==xp2:
    return (xp1,yp)
  if yp1==yp2:
    return (xp,yp1)
  xm=xp1-xp2
  ym=yp1-yp2
  x=((xm**2)*xp+(ym**2)*xp1-xm*ym*(yp1-yp))/(xm**2+ym**2)
  y=((xm**2)*ym*yp1-xm*(ym**2)*(xp1-xp)+(ym**3)*yp)/((xm**2)*ym+ym**3)
  return (x,y)
