s1 = 'hello'
s2 = 'world'
print(s1,id(s1))
print(s2,id(s2))
print(id(s1[0]))
print("Address of 'o in s1 is:", id(s1[1]))
print(s1,id(s1))
print("Address of 'o' in s2:", id(s2[1]))
print(s2,id(s2))
print('Address of l in s1: ', id(s1[2]))
print("Address of l in s1: ", id(s1[3]))
print('address odfl in s2: ', id(s2[3]))

print("Address od o in s1 is: ", id(s1[4]))
print("Address of o in s2 :", id(s2[1]))