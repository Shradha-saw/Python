import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(2)

def print_characters():
    for i in ['a', 'b', 'c', 'd']:
        print(i)
        time.sleep(1)

print_numbers()
print_characters()
       