li = [1,2,3,4,5,]

def square(ele):
    return ele ** 2

def cube(ele):
    return ele ** 3

square_list = list(map(square,li))
print("squate of li", square_list)

cube_list = list(map(cube, li))
print("cube of li", cube_list)