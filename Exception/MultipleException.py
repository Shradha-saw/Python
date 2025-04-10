def process(a,b):
    print(a/b)


try:
    process(12,0)
except ZeroDivisionError: #exception class
    print('ZeroDivisionError and Handled')

except NameError:
    print('Name error occured and handled')

except TypeError:
     print('Type Error occurred and Handled')

except:
    print('some exception occured and haldled')

print("Next  task")