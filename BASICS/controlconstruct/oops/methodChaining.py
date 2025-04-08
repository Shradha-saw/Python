class GrandParent:
    def cook(self):
        print("Grandparent cooks Roti")

class Parent(GrandParent):
    def cook(self):
        print("Parent cook maggie")

class Child(Parent):
    def cook(self):
        print("Child cooks maggie")
        super().cook()
        super(Parent,self).cook()#GrandPArent cook roti
c = Child()
c.cook()


class GreatGrandparent:
    def cook(self):
        print('Ggparent cook veggies')
class GrandParent(GreatGrandparent):
    def cook(self):
        print("Grandparent cooks Roti")

class Parent(GrandParent):
    def cook(self):
        print("Parent cook maggie")

class Child(Parent):
    def cook(self):
        print("Child cooks maggie")
        super().cook()
        super(Parent,self).cook() #GrandPArent cook roti
        super(GrandParent,self).cook() #greatgarpents cook vegies
c = Child()
c.cook()
