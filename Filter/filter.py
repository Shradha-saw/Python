# li = list(eval(input('enter comma seperated elements ')))
# even_li = []
# def even(li):
#     for i in li:
#         if i % 2 == 0:
#             even_li.append(i)

# even(li)
# print('Even list: ', even_li)

li = list(eval(input('Enter comma seperated elements')))
print('Original List', li)

def even(ele):
    if ele % 2 == 0:
        return ele
    
even_li = list(filter(even,li))
print('Even List: ', even_li)
    