class Demo:
    def __init__(self):
        self.__x = 100
    def disp(self):
        print(self.__x)

d = Demo()
d.disp()
print("Accessimg pvt var outside the class:", d._Demo__x)