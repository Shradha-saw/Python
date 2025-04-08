class Employee:
    def __init__(self,name,id):
        self.emp_name = name
        self.emp_id = id

#Creating obj:
e1 = Employee('Ak',101)
e2 = Employee('sk',102)

#accessing properties of e1 object
print('Employee name of e1 is :' , e1.emp_name)
print('Employee id od e1 is: ', e1.emp_id)

#accessing properties of e2 objects
print('Employee name of e1 is :' , e2.emp_name)
print('Employee id od e1 is: ', e2.emp_id)