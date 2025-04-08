class Demo1:
    def __init__(self):
        self.x = 100

class Demo2:
    def __init__(self):
        self.x = 200

class Demo3(Demo1, Demo2):
    pass
d3 = Demo3()
print(d3.x)

