n = 5
arr = [[" " for _ in range(n)] for _ in range(n)]

for i in range(n):
    # Place values along the diagonals
    arr[i][i] = str(i + 1) + str(i + 1)
    arr[i][n - 1 - i] = str(i + 1) + str(n - i)

for row in arr:
    print(' '.join(row))

#OUTPUT IS
'''11        15
     22   24
       33
     42   44
   51        55'''

