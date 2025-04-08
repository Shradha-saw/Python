s1 = {10,20,20,True,'code'}
print(s1,type(s1))

s1.add(500)
print(s1)

s1.remove(500)
print(s1)
#s1.add(600)
#s1[20] = 400 not support index element

#Union 

st1 = {1,2,3}
st2 = {3,4,5,6}
newset = st1.union(st2)
print(newset) #{1,2,3,4,5,6}
'''
set is also stored  homogenus as well as heterogenus tyes of data.

set is an unordered colln of data becs set generates the output in random order.It does not maintain order of inseration in output.

set does not allow duplicate values.

set is mutable means once we declare set, we can modify it.

'''