from cmp import cmp
#from polynomial import polynomial
from math import log, ceil, pi


def FFT(P):
  n = len(P)

  if n == 1:
    return P

  if log(n, 2) % 1 != 0:
    P += [0 for _ in range(2 ** ceil(log(n, 2)) - n)]
    n = 2 ** ceil(log(n, 2))

  w = cmp.cmpexp(2 * pi / n)

  Pe, Po = P[::2], P[1::2]
  ye, yo = FFT(Pe), FFT(Po)

  y = [0] * n
  
  for i in range(n // 2):
    y[i] = ye[i] + w ** i * yo[i]
    y[i + n // 2] = ye[i] - w ** i * yo[i]

  return y


def IFFT(P):
  n = len(P)

  if n == 1:
    return P

  if log(n, 2) % 1 != 0:
    P += [(0, 0) for _ in range(2 ** ceil(log(n, 2)) - n)]
    n = 2 ** ceil(log(n, 2))

  w = cmp.cmpexp(-2 * pi / n) / n

  Pe, Po = P[::2], P[1::2]
  ye, yo = IFFT(Pe), IFFT(Po)

  y = [0] * n

  for i in range(n // 2):
    y[i] = ye[i] + w ** i * yo[i]
    y[i + n // 2] = ye[i] - w ** i * yo[i]

  return y


a = FFT([0, 1, 2])
b = IFFT([i for i in a])

print(', '.join([f'({str(i)})' for i in a]))
print(', '.join([f'({str(i)})' for i in b]))