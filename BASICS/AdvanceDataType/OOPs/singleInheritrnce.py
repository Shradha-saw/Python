class Demo1:
    def disp1(self):
        print("disp1")

class Demo2 (Demo1):
    def disp2(self):
        print("disp2")

d2 = Demo2()
d2.disp2()
d2.disp1()