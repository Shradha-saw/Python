class Demo1:
    def magic(self):
        print('Inside magic method  of Demo1')

class Demo2:
    def magic(self):
        print("Inside magic method of Demo2")

class Demo3(Demo1, Demo2):
    pass

d3 = Demo3()
d3.magic()
print(Demo3.__mro__)