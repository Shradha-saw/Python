class Demo:
    def __init__(self):
        self.name = "Shradha"

d1 = Demo()
print(d1.name) #Accessing public property outside the class allowed


class Demo1(Demo):
    def disp(self):
        print(self.name)#Accessing public property inside child class allowed

dm1 = Demo1()
dm1.disp()

class code:
    def display(self):
        print(d1.name) # Accessing public property iside non child class allowed

c = code()
c.display()