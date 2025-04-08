class Demo1:
    def disp1(self):
        print("disp1")

class Demo2(Demo1):
    def desp2(self):
        print("disp2")

class Demo3(Demo1):
    def disp3(self):
        print("Disp3")

d3 = Demo3()
d3.disp1()

d2 = Demo2()
d2.disp1()