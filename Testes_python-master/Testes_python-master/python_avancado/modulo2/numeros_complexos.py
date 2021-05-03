class Complexo:
    def __init__(self, r, i):
        self.r =r
        self.i = i

    def __repr__(self):
        return "({}, {}i)".format(self.r, self.i)

    def __add__(self, other):
        return Complexo(self.r + other.r, self.i + other.i)

c1 = Complexo(1, 3)
print(c1)
c2 = Complexo(3, 5)
c3 = c1 + c2
print(c3)