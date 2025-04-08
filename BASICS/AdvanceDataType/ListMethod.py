#add element into list
li= [50]
li.append(100)
print(li) #[50, 100]
#insert (index, element ) inserts an elemnet at spectfic index
li.insert(0, 500)
print(li)#[500,50,100]


# POP():  Pop method without any argument removes anf return last element fron the list
ele = li.pop()
print(ele) #100
print(li) #[500, 50]

#pop(index): pop can remove specific index elemnet from list.

print(li.pop(0)) #500
print(li) #[50]


li.append(700) 
print(li)#[50, 700]
#remove(element): Removes element from lists.
li.remove(700)
print(li) #[50] 

li.append(900) #[50,900]
#del keywoed: 
del li[1]
print("After del: ", li) # [50]

del li #deletes whole object from the memory.
# print(li) #Error