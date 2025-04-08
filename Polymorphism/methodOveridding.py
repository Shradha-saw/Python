class Parent:
    def cook(self):
        print("Cooking Briyani")
    def learn(self):
        print("Learning maths")


class Child(Parent):
    def play(self):
        print('Playing Cricket')

    def learn(self):
        print("Learning Python")

c = Child()
c.cook()

'''
The method whuich is derived from parent class and used as it is in child class, we call it as Inherited method.
'''

'''
The method which is only avaliable for child class anf not for parent class,  such methods are called as speclaised methods
'''

'''
The methods which are derived form p[arent class and Modified into chils class as per 
child class requriment, such methods are called as overridden methods]
'''