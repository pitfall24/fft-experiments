from cmp import cmp
#from polynomial import polynomial
from math import log, e, pi, ceil


def FFT(P):
  n = len(P)

  if n == 1:
    return P

  if log(n, 2) % 1 != 0:
    P += [0 for _ in range(2 ** ceil(log(n, 2)) - n)]

  print(P)

  w = cmp(e, 0)**(2 * pi * cmp(0, 1) / n)

  Pe, Po = P[::2], P[1::2]
  ye, yo = FFT(Pe), FFT(Po)

  y = [0] * n

  for i in range(n // 2):
    y[i] = ye[i] + w**i * yo[i]
    y[i + n // 2] = ye[i] - w**i * yo[i]

  return y


def IFFT(P):
  n = len(P)

  if n == 1:
    return P

  if log(n, 2) % 1 != 0:
    P += [(0, 0) for _ in range(2 ** ceil(log(n, 2)) - n)]

  w = cmp(e, 0)**(-2 * pi * cmp(0, 1) / n) / n

  Pe, Po = P[::2], P[1::2]
  ye, yo = IFFT(Pe), IFFT(Po)

  y = [0] * n

  for i in range(n // 2):
    y[i] = ye[i] + w**i * yo[i]
    y[i + n // 2] = ye[i] - w**i * yo[i]

  return y


a = FFT([0, 1])

print(', '.join([f'({str(i)})' for i in a]))
