#OPERATOR OVERLOADING
class Vect:

  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vect(self.i + x.i, self.j + x.j, self.k + x.k)


v1 = Vect(1, 4, 7)
print(v1)
v2 = Vect(6, 4, 2)
print(v2)
v3 = Vect(3, 6, 9)
print(v3)
print(v1 + v2 + v3)