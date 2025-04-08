#iterable obj means group of values
li = [10,20,30,40]
for i in li:
    print(i)
#wap to print sq of each elemeent of li in list.
for i in li:
    print(i ** 2)

for i in li:
    print(i ** 4)

# sample input[10,20,30,40]
# sample output[100,200,300,400]

print()

li1 = [2,3,4,5,6]
sq = []

for i in li1:
    sq.append(i**2)

print('Square list is: ', sq)


print([i**2 for i in li])
#[expression for control_variable in iterable object]
li3 = [1,2,3,4]
ref = [i for i in li3]
print(ref)
print()
#wap to add +5 to each e;ement of li and create new list of it.
a = [9,8,7]
print([i+5 for i in a])

print()

#wap to print of even elements from lists
lists = [1,2,3,4,5,6,7]
print([i for i in lists if i % 2 == 0]) # expression for control variable in iterable object condition

print()

#wap to print of odd elements from B
B = [1,2,3,4,5,6,7,8,9]
print([i for i in B if i % 2 != 0])