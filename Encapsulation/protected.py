class Demo1:
    def __init__(self):
        self._name = 'Sk' #protected variable
    def disp1(self):
        print(self._name)#Accessinf inside the same class

d1 = Demo1()

class Demo2(Demo1):
    def disp(Self):
        print(Self._name) #Accessing inside the chils class

d2 = Demo2()
