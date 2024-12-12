i=1
j=1
n=3
print(i,j)
for x in range(0,n-1):
    while True:
        if j<(n-x):
            j+=1
            print(i,j)
        else:
            break
    while True:
        if i<(n-x):
            i+=1
            print(i,j)
        else:
            break
    while True:
        if j>x+1:
            j-=1
            print(i,j)
        else:
            break
    while True:
        i-=1
        if i-j>0:
            print(i,j)
        else:
            i+=1
            break

'''
i and j represent the current row and column positions, starting at (1,1).
n is the grid size, set to 3, meaning the grid is 3x3.
The first position (1,1) is printed.
Outer Loop:for x in range(0, n-1) 
controls the number of layers in the spiral traversal. For a grid of size n=3, there are n-1=2 layers to traverse.

Inner While Loops: Each while loop 
responsible for moving in one direction in the grid:

Right Movement: while j < (n - x):
Increases the column index j as long as j is within the current boundary (n-x).
Prints the updated position (i, j).

Down Movement:while i < (n - x):
Increases the row index i while staying within the current boundary (n-x).
Prints the updated position (i, j).

Left Movement:while j > x + 1:
Decreases the column index j as long as it stays above the left boundary (x+1).
Prints the updated position (i, j).

Up Movement:while True: (with a condition inside the loop)
Decreases the row index i.
Breaks when the diagonal condition i-j > 0 is no longer true, effectively stopping the upward traversal.'''
