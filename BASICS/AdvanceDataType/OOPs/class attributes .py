class Emp:
    college_name = 'Sjbit'
    def __init__(self, name):
        self.name = name

e1 = Emp('Akash')
e2 = Emp('Ankit')
# class level variables can be accessed using object ref or class name
''''
class vs instance variables:

class level variables are such variavbles which are declared inside the class and outside any method

all obj for that class sghare same copy of class variables.

Instance variables are such variables which are present inside objects.
For each obj seperates  copy of instance varibles will be created
'''
print(e1.college_name)
print(e2.college_name)
print(Emp.college_name)