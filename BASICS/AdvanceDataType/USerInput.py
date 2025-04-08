userdata = input('Enter lsit elements seperated by space')#'10,20,30,40'
li = userdata.split()
print(li)#['10', '20', '30']
newli = []
for i in li:
    newli.append(int(i))
print(newli)

print(sum(newli)/len(newli))

#
userdatas = input('enter the ele').split()
a = []
for i in a:
    a.append(int(i))
print(sum(a)/len(a))