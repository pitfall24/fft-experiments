class polynomial:
  def __init__(self, vars):
    if isinstance(vars, list):
      raise TypeError("polynomial constructor takes a list")
    elif isinstance(vars[0], list) or isinstance(vars[0], tuple):
      self.coeff = [None for _ in range(len(vars))]
      self.points = [(i[0], i[1]) for i in vars]
    else:
      self.coeff = [i for i in vars]
      self.points = [None for _ in range(len(vars))]

  def __getitem__(self, key):
    if isinstance(key, slice):
      return [self.points[i] for i in range(*key.indices(len(self.points)))]
    else:
      return self.points[key]

  def __setitem__(self, key, value):
    if isinstance(key, slice):
      for i in range(*key.indices(len(self.points))):
        self.points[i] = value
    else:
      self.points[key] = value
