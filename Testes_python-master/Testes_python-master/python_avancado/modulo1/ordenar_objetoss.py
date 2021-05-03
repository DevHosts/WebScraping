
from operator import attrgetter

class Objeto:
    def __init__(self, obj_id):
        self.obj_id = obj_id

    def __repr__(self):
        return str(self.obj_id)

objeto1 = [Objeto(90), Objeto(15), Objeto(20)]
print(objeto1)

class Objeto2:
    def __init__(self, ob):
        self.ob = ob

    def __repr__(self):
        return str(self.ob)

o = [Objeto2(3), Objeto2(6), Objeto2(9)]
print(sorted(o, key=attrgetter('ob')))