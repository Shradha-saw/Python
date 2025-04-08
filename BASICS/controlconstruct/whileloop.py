#wac to print numbers from 1-10
i = 1
while(i < 10):
    print(i)
    i = i+1

print()
#wac to print numberss from 1-5 but if number is equal to 3 dont print it
for j in range(1,6):
    if(j == 3):
        continue
    else:
        print(j)


print()

#wac to print numbers from 1-10 but if number is equal to 5 then break the loop
for k in range(1,11):
    if(k == 5):
        break
    else:
        print(k)

print()
# table of given number in one linr seprated by space
num = int(input('Enter the num of table'))
for b in range(1,11):
    print(b * num, end=" ")  