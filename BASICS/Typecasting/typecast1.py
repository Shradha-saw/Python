#converting one type of data into another type
#int();
a = '10'
print(a, type(a))
b = int(a)
print(b, type(b))

#print(int('100'))
#print(int('120.77'))
#----------------------------------------------------------------------------------------------------------------
# string to int conversion
#in python while converting str to int , only when str is holding int value to int conversion is allowed
print(int('12'))
# print(int('code'))#error
# print(int('12.44'))#error
# print(int('true'))#error

#wac to take 2 float numbers from user and display its addition
c = 12.22
d = 10.2
print(c + d)

num1 = float(input('enter num1'))
num2 = float(input('enter num2'))
print(num1, type(num1), num2 , type(num2))
print('addition is: ', round(num1 + num2,1))