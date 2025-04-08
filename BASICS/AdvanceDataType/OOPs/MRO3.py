class Demo1:
    def __init__(self):
        self.x = 100
class Demo2:
    def __init__(self):
        self.x = 200
        super().__init__()
class Demo3(Demo2, Demo1):
    pass
d3 = Demo3()
print(d3.x)

class Demo4:
    def __init__(self):
        self.x = 100
        super().__init__()
class Demo5:
    def __init__(self):
        self.x = 200
        super().__init__()
class Demo6(Demo4, Demo5):
    pass
d6 = Demo6()
print(d6.x)

