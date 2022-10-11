class cchar:
  def __init__(self):
    self._val=0
    return

  def __init__(self,val):
    if type(val)==int:
      self._val=val
    elif type(val)==str and len(val)==1:
      self._val=ord(val)
    elif type(val)==cchar:
      self._val=cchar._val
    else:
      raise TypeError("The value type must be int or str(1).")
    return

  def __add__(self,other):
    if type(other)==cchar:
      return cchar(self._val+other._val)
    elif type(other)==int:
      return cchar(self._val+other)
    elif type(other)==str and len(other)==1:
      return cchar(self._val+ord(other))
    else:
      raise TypeError

  def __sub__(self,other):
    if type(other)==cchar:
      return cchar(self._val-other._val)
    elif type(other)==int:
      return cchar(self._val-other)
    elif type(other)==str and len(other)==1:
      return cchar(self._val-ord(other))
    else:
      raise TypeError

  def __mul__(self,other):
    if type(other)==cchar:
      return cchar(self._val*other._val)
    elif type(other)==int:
      return cchar(self._val*other)
    elif type(other)==str and len(other)==1:
      return cchar(self._val*ord(other))
    else:
      raise TypeError

  def __truediv__(self,other):
    if type(other)==cchar:
      return float(self._val/other._val)
    elif type(other)==int:
      return float(self._val/other)
    elif type(other)==str and len(other)==1:
      return float(self._val/ord(other))
    else:
      raise TypeError

  def __floordiv__(self,other):
    if type(other)==cchar:
      return cchar(self._val//other._val)
    elif type(other)==int:
      return cchar(self._val//other)
    elif type(other)==str and len(other)==1:
      return cchar(self._val//ord(other))
    else:
      raise TypeError

  def __mod__(self,other):
    if type(other)==cchar:
      return cchar(self._val%other._val)
    elif type(other)==int:
      return cchar(self._val%other)
    elif type(other)==str and len(other)==1:
      return cchar(self._val%ord(other))
    else:
      raise TypeError

  def __pow__(self,other):
    if type(other)==cchar:
      return cchar(self._val**other._val)
    elif type(other)==int:
      return cchar(self._val**other)
    elif type(other)==str and len(other)==1:
      return cchar(self._val**ord(other))
    else:
      raise TypeError

  def __lt__(self,other):
    if type(other)==cchar:
      return self._val<other._val
    elif type(other)==int:
      return self._val<other
    elif type(other)==str and len(other)==1:
      return self._val<ord(other)
    else:
      raise TypeError

  def __le__(self,other):
    if type(other)==cchar:
      return self._val<=other._val
    elif type(other)==int:
      return self._val<=other
    elif type(other)==str and len(other)==1:
      return self._val<=ord(other)
    else:
      raise TypeError

  def __gt__(self,other):
    if type(other)==cchar:
      return self._val>other._val
    elif type(other)==int:
      return self._val>other
    elif type(other)==str and len(other)==1:
      return self._val>ord(other)
    else:
      raise TypeError

  def __ge__(self,other):
    if type(other)==cchar:
      return self._val>=other._val
    elif type(other)==int:
      return self._val>=other
    elif type(other)==str and len(other)==1:
      return self._val>=ord(other)
    else:
      raise TypeError

  def __eq__(self,other):
    if type(other)==cchar:
      return self._val==other._val
    elif type(other)==int:
      return self._val==other
    elif type(other)==str and len(other)==1:
      return self._val==ord(other)
    else:
      raise TypeError

  def __ne__(self,other):
    if type(other)==cchar:
      return self._val!=other._val
    elif type(other)==int:
      return self._val!=other
    elif type(other)==str and len(other)==1:
      return self._val!=ord(other)
    else:
      raise TypeError

  def __iadd__(self,other):
    if type(other)==cchar:
      self._val+=other._val
      return cchar(self._val)
    elif type(other)==int:
      self._val+=other
      return cchar(self._val)
    elif type(other)==str and len(other)==1:
      self._val+=ord(other)
      return cchar(self._val)
    else:
      raise TypeError

  def __isub__(self,other):
    if type(other)==cchar:
      self._val-=other._val
      return cchar(self._val)
    elif type(other)==int:
      self._val-=other
      return cchar(self._val)
    elif type(other)==str and len(other)==1:
      self._val-=ord(other)
      return cchar(self._val)
    else:
      raise TypeError

  def __imul__(self,other):
    if type(other)==cchar:
      self._val*=other._val
      return cchar(self._val)
    elif type(other)==int:
      self._val*=other
      return cchar(self._val)
    elif type(other)==str and len(other)==1:
      self._val*=ord(other)
      return cchar(self._val)
    else:
      raise TypeError

  # def __itruediv__(self,other):
  #   if type(other)==cchar:
  #     self._val/=other._val
  #     return cchar(self._val)
  #   elif type(other)==int:
  #     self._val/=other
  #     return cchar(self._val)
  #   elif type(other)==str and len(other)==1:
  #     self._val/=ord(other)
  #     return cchar(self._val)
  #   else:
  #     raise TypeError

  def __ifloordiv__(self,other):
    if type(other)==cchar:
      self._val//=other._val
      return cchar(self._val)
    elif type(other)==int:
      self._val//=other
      return cchar(self._val)
    elif type(other)==str and len(other)==1:
      self._val//=ord(other)
      return cchar(self._val)
    else:
      raise TypeError

  def __imod__(self,other):
    if type(other)==cchar:
      self._val%=other._val
      return cchar(self._val)
    elif type(other)==int:
      self._val%=other
      return cchar(self._val)
    elif type(other)==str and len(other)==1:
      self._val%=ord(other)
      return cchar(self._val)
    else:
      raise TypeError

  def __ipow__(self,other):
    if type(other)==cchar:
      self._val**=other._val
      return cchar(self._val)
    elif type(other)==int:
      self._val**=other
      return cchar(self._val)
    elif type(other)==str and len(other)==1:
      self._val**=ord(other)
      return cchar(self._val)
    else:
      raise TypeError

  def __pos__(self):
    return cchar(self._val)
  
  def __neg__(self):
    return cchar(-self._val)

  def __invert__(self):
    return cchar(~self._val)

  def __str__(self):
    return chr(self._val)

  def __repr__(self):
    return f"cchar({self._val})"

  def __int__(self):
    return self._val
  
  def int(self):
    return self._val



