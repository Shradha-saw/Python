#Q. can we return multiple values from  function using return statement? no

def process():
    return 10
    return 20
    return 30

res = process()
print(res) #10

# Can we return multiples values from a function using yield keyword? yes

def disp():
    yield 10
    yield 20
    yield 30

result = disp()
print(result) # Generator object
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())#stop iteration
