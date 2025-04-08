class Demo1:
    def disp1(self):
        print('disp1')

class Demo2(Demo1):
    def disp2(self):
        print("disp2")

class Demo3(Demo2):
    def disp3(self):
        print("disp3")

d3 = Demo3()
d3.disp3()
d3.disp2()
d3.disp1()