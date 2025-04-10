def add(a,b):
    print("Start")
    print(a/b)
    print("End")

try:
    add(10,0)
except:
    print("Exception handling ccured!!")

print('Other task')

def div(c,d):
    print("start")
    print(c/d)

try:
    div(10,5)

except:
    print('Exception occured and handle')

else:
    print('There is no exception')

finally:
    print("End")

print('other tasks')