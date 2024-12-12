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
 return result.zfill(max_len)
compl2=add('1')
print("subtraction is: ",add('110010',compl2))

'''README:
compl1() Function: computes the 1's complement of a binary number a, which is fixed here as 100110.
Logic:Converts the integer 100110 to a list of digits: [1, 0, 0, 1, 1, 0], iterates through the digits and replaces 0 with 1 and 1 with 0.
Output: The 1's complement of 100110 is returned as a string: 011001

add() Function: This function performs binary addition.
Parameters:
a: A binary string.
b: result from compl1() (011001).
Logic:
Padding of both binary strings to the same length using zfill.
Iterates from the least significant bit (rightmost) to the most significant bit (leftmost):
Adds corresponding bits from a and b, including a carry.
Computes the result for each position using modulo (% 2) for the sum and determines the carry for the next iteration.
Returns the result as a binary string with the same length as the inputs.

compl2 = add('1')
Computes the 2's complement of 100110 by adding 1 to its 1's complement (011001).
Result:
1's complement: 011001
2's complement: 011010

print("subtraction is: ", add('110010', compl2))
Simulates binary subtraction by adding the 2's complement of a number.
Logic:
To subtract 100110 from 110010:
Take the 2's complement of 100110 (011010).
Add it to 110010 using the add() function.
Result:
110010 + 011010 = 1000000 '''
