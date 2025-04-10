def smartdiv(function):
    def inner(a,b):
        if b == 0:
            print('Not possible')
        else:
            return function(a,b)
        
    return inner
@smartdiv
def div(a,b):
    print(a/b)

div(10,2)
print(20,5)
div(10,0  )
