class Employee:
    name = 'shradha' # class level variables
    age = 33

    def teach(self):
        print("Employee is teaching")
e1 = Employee()
e2 = Employee()

print(e1.name)
print(e2.name)
e1.teach()
e2.teach


'''
1. The method which are present inside the class are called as instance(object) methods.
2. For instance methods self parameter is must.
'''

class Users:
    bankname = 'SBI'
    def deposit (self):
        print("Deposite method")
    def withdraw(self):
        print("Withdraw method")

u1 = Users()
u1.name = "Shr"
u1.AccNo = 4202

u2 = Users()
u2.name = "Nisha"
u2.Accno = 4203


class Empo:
    companyName = "COde"
    def work(self):
        print(self.name,' is working')
    def play(self):
        print(self.name, ' is playing')

em = Empo()
em.name = 'Ak'
em.id = 101
em.work()

em = Empo()
em.name ='Pk'
em.id = 102    
em.work()
em.play()
# self will always hold add of current object
# the variavle whic are present inside an object such variavle are called as instance Variables.
# For instance variables seperate copy owill be created for each object.
# Class Level varaibles 
# self parameter