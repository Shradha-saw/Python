li = [1,2,3,4]

def square(ele):
    return ele * ele

result = map(square, li)
print(result)#map objext at

print(list(result))#[1, 4, 9, 16]

li2 = ['10', '20', '30']
print(li2)#'10', '20', '30']
new_li = list(map(int,li2))
print(new_li)#[10, 20, 30]

li1 = [1,2,3,4]
new_lii = list(map(float,li))
print(new_lii)
print(list(map(bool,li1)))