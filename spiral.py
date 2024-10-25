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