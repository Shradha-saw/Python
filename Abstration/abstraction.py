from abc import ABC, abstractmethod
'''
Rule: 1 we can create an object for empty abstract class
'''

class Animal(ABC):
    pass
a1 = Animal()

'''
Rule 2: if  abstract class contains method then objects 
fot that abstracr clas can't be created and abstract method cannot be invoked. 
'''
class Animal2(ABC):
    @abstractmethod
    def eat(Self):
        pass
#a2 = Animal()

'''
Rule 3 If abstract class contains only concreate metods, then object can be created and
concrete method can be invoked.
'''
class Animal3(ABC):
    def eat(self):
        print('Inside eat')
a3 = Animal3()
a3.eat()

'''
Rule 4: If class is derived form abstract class and not given body
for all abstract methods in child class then child class object cannot be created
'''
class Animal4(ABC):
    @abstractmethod
    def eat(Self):
        pass
    @abstractmethod
    def sleep(Self):
        pass

class Child(Animal4):
    def eat(self):
        print('Inside eat')

#c = Chils() not allowed