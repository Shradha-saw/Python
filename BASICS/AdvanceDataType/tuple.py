t1 = (10,20,30,40,True,'code')
print(t1)

print(t1, type(t1))

#accessing specific elemnet from tuple:
print(t1[0]) # 10
print(t1[3]) # True

#t1[0] = 300 //ot allowed
#print(t1)

'''
1. tuple is an advance data structure in python
Tuple can store both homogenus and heterogenus type of data

2. Tuple is an ordered colln of data.

3. Tuple stores duplicate values.

4.Tuple is immutable(once we create we cannot modify)
'''
#Unpacking the tuple-----------------------------
t2 = (100,200,300,400)
e1, e2, e3, e4 = t2
print(f'el: {e1}, e2: {e2}, e3: {e3}, e4: {e4} ')

tup1 = (10,20)
tup2 = (30,40)
newtup = tup1 + tup2 #(10,20,30,40)
print(newtup)#(10,20,30,40)
print(len(newtup)) #4