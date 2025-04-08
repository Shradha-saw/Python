def add(a,b): #def is a keyword to define a funcion
    print('Inside add method')
    print("Addition is: ", a+b)

add(10,20)    
#func without parameter and return statemnet
def greet():
    print('Good night...!!')
greet()  

#func without paramenter and with return statemnet
def greet1():
    return "Hello, Good night "
res = greet1()
print(res)    

def addi():
    x = 10
    y = 20
    z = 30 
    print(x+y+z)
addi()

def sum(g,h):
    return g + h
result = sum(20,30)
print(result)

def names(name):
    print('Hello',name)

names('shradha')
names('isha')


def addition():
    u = int(input("enter a value u: "))
    v = int(input("enter a value u: "))
    print(u + v)
addition()

def addition1(q,w):
    print(q + w)
q = int(input(" enter value"))
w = int(input("enter value "))
addition1(q,w)    