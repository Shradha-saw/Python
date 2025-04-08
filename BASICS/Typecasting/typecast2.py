#bool();
print(bool(12)) # 1 true -- int to bool conv
print(bool(12.345)) #1 true -- float to bool conv
print(bool('code')) # true --str hold str to bool
print(bool(0)) # false  -- int to bool
print(bool('')) #false\ empty str to bool

#float();
print(float(123)) #123.0-- int to float conversion
# print(float('code')) error-- string holding str to float
print(float('123.23')) #123.33 str holding float to float
print(float(True)) # 1.0 bool to float conversion
print(float(False)) #0.0 bool to float conv

#int();
print(int(123.55))#FLOAT TO INT CONVERSION
print(int('123'))# SRT HOLDING INT TO INT ALLOWED
print(int(True))#BOOLEAN TO  INT 
print(int(False))#BOOLEAN TO INT
#print(int('code'))#STR HOLD STR TO INT ERROR
#print('123.45')#STR HOLD FLOAT TO INT ERROR
