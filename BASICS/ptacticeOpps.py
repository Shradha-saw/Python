# class Employee:
#     name = "Shradha"
#     age = 33

#     def teach(self):
#         print('Employrr is Teaching')
    

# e1 = Employee()
# e2 = Employee()
 
# print(e1.name)
# print(e2.name)
# e1.teach()
# e2.teach()

class Employee:
    company_name = 'Code'

    def work(self):
        print("Employee is working")

    def study(self):
        print("Employee is playing")

e1 = Employee()
e1.name = "Shradha"
e1.id = 102
e1.work()

e2 = Employee()
e2.name = "Suchi"
e2.id = 102
e2.study()
e1.work()
print(e2.name)


