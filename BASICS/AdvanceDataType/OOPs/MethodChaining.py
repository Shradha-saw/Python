class GreatGrandParent:
    def cook(self):
        print("Grandparents cooks ABC")

class GrandParents:
    def cook(self):
        print("GrandParent cooks Briyani")

class Parent(GrandParents):
    def cook(self):
        print("Parents cooks pulao")

class Child(Parent):
    def cook(self):
        print("Child cooks maggie")
        super().cook()#Parents cooks pulao
        super(Parent,self).cook() #GrandParent cooks Briyani
        super(GrandParents.self).cook()
c = Child()
c.cook()
#method chaing is the process calling one method to another method