class Car():
    def create(self):
        print("I am a car")
class Avtomat(Car):
    def v(self):
        print("aragutyun")
    def create(self):
        print("Avtomat object")
class Mexanikakan(Car):
    def v(self):
        print("aragutyun")
    def create(self):
        print("Mexanikakan object")
class BMW(Avtomat):
    def __init__(self, a):
        super().__init__()
        self.a = a
    def v(self):
        return self.a
    def create(self):
        print("Avtomat")
class Maskvich(Mexanikakan):
    def __init__(self, b):
        super().__init__()
        self.b = b
    def w(self):
        return self.b
    def create(self):
        print("Mexanikakan")
p1 = BMW(180)
print(p1.v)
p1.create()
p2 = Maskvich(0.00000001)
print(p2.w)
p2.create()