d1 = {'name' : 'Priya' ,
       'age': 33,
       'phone' : 34568,
       'Maths' : 90,
       'Science' : 90,
       'name': 'shrdha'
    
      }
print(d1, type(d1))
#Accessing element
print(d1['name']) #Shradha
print(d1['Maths']) #90
#################################################
for i in d1.keys():
    print(i)

print()
for i in d1.values():
    print(i, end = "-")
####################################################
for i in d1.items():
    print(i)
'''
    ('age', 33)
('phone', 34568)
('Maths', 90)
('Science', 90)
'''
'''
1. Dict can store both homogenus and hetrogenus
'''