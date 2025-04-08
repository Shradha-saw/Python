class Employee:
    #constructor with fixed name __init__
    def __init__(self): #construcror with class name
        self.emp_name = 'ak' #Instance variables
        self.emp_id = 101  #instance variables

    #Creating objects:
e1 = Employee()
    
    #Accessing properties of e1 objects:
print('Employee name is: ',e1.emp_name)
print('Employee ID is:', e1.emp_id)