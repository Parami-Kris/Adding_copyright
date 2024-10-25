def compl1():
 a=100110
 b=list(map(int,str(a)))
 for i in range(0, len(b)):
    if (b[i]==0):
        b[i]=1
    elif(b[i]==1):
        b[i]=0
 r=str(b[0])
 for j in range(1,len(b)):
    r+=str(b[j])
 return r
compl1()
def add(a,b=compl1()):
 max_len = max(len(a), len(b))
 a = a.zfill(max_len)
 b = b.zfill(max_len)
 result = ''
 carry = 0
 for i in range(max_len - 1, -1, -1):
    r = carry
    r += 1 if a[i] == '1' else 0
    r += 1 if b[i] == '1' else 0
    result = ('1' if r % 2 == 1 else '0') + result
    carry = 0 if r < 2 else 1
 if carry != 0:
    result = '1' + result
 return result.zfill(max_len)
print("2's complement of 101101 is: ",add('1'))