from cmp import cmp
from math import cos, sin, pi

# does cmp.angle / atan functionality actually work

print("[", end="")

for i in range(1000):
  theta = i * pi / 500
  x, y = cos(theta), sin(theta)
  print(f'({theta}, {cmp.angle(x, y)})', end=', ')

print("]")


# do the complex number operations defined in cmp work correctly

a = cmp(3, 4)
b = cmp(2, -1)

for i in range(100):
    t = a ** (i / 20)
    print(f'({t.a}, {t.b})')

print(a / b)
print(a * b)
print(a ** b)
print(a ** (b * ~b))
print(4 / a + b)
