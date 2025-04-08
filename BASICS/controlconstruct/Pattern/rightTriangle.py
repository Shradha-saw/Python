rows = int(input('Enter Rows: '))
col = int(input('Enter col: '))
for i in range(rows):
    print("* " * col)

rowss = int(input('enter rows: '))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#Increasing pattern
roow = int(input('Enter number of rows'))
for i in range(rows):
    for j in range(i + 1):
        print('*', end= " ")
    print()

#decreasing pattern
roow = int(input('Enter number of rows: '))
for i in range(rows):
    for j in range(i, roow):
        print('*', end= " ")
    print()
# Diamond pattern---------------------------------
#hill pattern
r = int(input('Enter number of rows'))
for i in range(r):
    for j in range(i, r):
        print(" ", end=" ")
    for k in range(i + 1):
        print('*', end=" ")
    for l in range(i):
        print('*', end=" ")
    print()
#Lower hill
rowsss = int(input())
for i in range(rowsss):
    for j in range(i+1):
        print(' ',end=" ")
    for k in range(i, rowsss):
        print('*', end=" ")
    for m in range(i,rowsss):
        print('*', end=" ")
    print()

#Pascal pattern------------


