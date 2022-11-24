import math

class cmp:
  def __init__(self, a, b=None):
    if b is not None:
      self.a = a
      self.b = b
    else:
      try:
        self.a = a.a
        self.b = a.b
      except AttributeError:
        self.a = a
        self.b = 0

  @staticmethod
  def angle(a, b=None):
    if isinstance(a, cmp):
      if a.a == 0:
        return math.pi / 2 if a.b > 0 else 3 * math.pi / 2
      elif a.a > 0:
        return math.atan(a.b / a.a) + (2 * math.pi if a.b < 0 else 0)
      else:
        return math.atan(a.b / a.a) + math.pi
    else:
      return cmp.angle(cmp(a, b))

  @staticmethod
  def cmpexp(a, b=None):
    if isinstance(a, cmp):
      return math.sqrt(a.a**2 + a.b**2) * cmp.cmpexp(cmp.angle(a, b))
    elif b is None:
      return cmp(math.cos(a), math.sin(a))
    else:
      return cmp.cmpexp(cmp(a, b))

  def __add__(self, a, b=None):
    if isinstance(a, cmp):
      return cmp(self.a + a.a, self.b + a.b)
    else:
      if b is None:
        b = 0
      return cmp(self.a + a, self.b + b)

  def __radd__(self, a, b=None):
    return self.__add__(a, b)

  def __sub__(self, a, b=None):
    if isinstance(a, cmp):
      return cmp(self.a - a.a, self.b - a.b)
    else:
      if b is None:
        b = 0
      return cmp(self.a - a, self.b - b)

  def __rsub__(self, a, b=None):
    return self.__sub__(a, b)

  def __mul__(self, a, b=None):
    if isinstance(a, cmp):
      return cmp(self.a * a.a - self.b * a.b, self.a * a.b + self.b * a.a)
    else:
      if b is None:
        b = 0
      return cmp(self.a * a - self.b * b, self.a * b + self.b * a)

  def __rmul__(self, a, b=None):
    return self.__mul__(a, b)

  def __truediv__(self, a):
    if isinstance(a, cmp):
      raise TypeError("can only divide by real numbers")
    else:
      return cmp(self.a / a, self.b / a)

  def __pow__(self, power):
    r = math.sqrt(self.a * self.a + self.b * self.b)
    try:
      theta = math.atan(self.b / self.a)
    except ZeroDivisionError:
      theta = (1 if self.b > 0 else -1) * math.pi / 2

    return r**power * self.exp(cmp(0, 1) * power * theta)

  def __rpow__(self, power):
    return self.__pow__(power)

  def __iadd__(self, a, b=None):
    if isinstance(a, cmp):
      return self + a
    else:
      return self + cmp(a, b)

  def __isub__(self, a, b=None):
    if isinstance(a, cmp):
      return self - a
    else:
      return self - cmp(a, b)

  def __imul__(self, a, b=None):
    if isinstance(a, cmp):
      return self * a
    else:
      return self * cmp(a, b)

  def __idiv__(self, a):
    return self / a

  def __ipow__(self, power):
    return self**power

  def __neg__(self):
    return cmp(-self.a, -self.b)

  def __pos__(self):
    return cmp(abs(self.a), abs(self.b))

  def __invert__(self):
    return cmp(self.a, -self.b)

  def __str__(self):
    return f'{self.a} + {self.b}i'


print("[", end="")

for i in range(1000):
  theta = i * math.pi / 500
  x, y = math.cos(theta), math.sin(theta)
  print(f'({theta}, {cmp.angle(x, y)})')

print("]")
