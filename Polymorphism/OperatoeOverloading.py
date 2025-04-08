class Student:
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name

s1 = Student("Pooja")
print(s1)

s2 = Student("shradha")
print(s2)



class Student:
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name
    
    def __truediv__(self, other):
        return self.name + other.name

s1 = Student("Pooja")
print(s1)

s2 = Student("shradha")
print(s2)

print(s1 / s2)
