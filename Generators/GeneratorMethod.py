def disp():
    print("Start")
    yield 10
    print("Task 1")
    yield 20
    print("Task 2")
    yield 30

res = disp()
#print(res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
#print(res.__next__())

# for i in range(3):
#     print(res.__next__())

for i in res:
    try:
        print(res.__next__())
    except:
        print("tHere is not next value available stop tis iteration")
