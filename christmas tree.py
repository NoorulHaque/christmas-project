# Online Python cwidth = int(input("Enter Chirstmas Tree Width   = "))
height = int(1)
width = 17
space = width * height
n = 1

print("The Chirstmas Tree Star Pattern")
alphabet = 65

for x in range(1, height + 1):
    for i in range(n, width + 1):
        for j in range(space, i - 1, -1):
            print(end=' ')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()
    n = n + 2
    width = width + 2

for i in range(1, height):
    for j in range(space - 3, -1, -1):
        print(end=' ')
    for k in range(1, height):
        print('*', end=' ')
    print()

    # leg of christmas tree

# Reading number of rows and columns
row = int(4)
col = int(2)

for i in range(1,int (( row + 1/2))):
    for j in range(1, col + 1):
        print('',end=' ')
    print('             * *')
