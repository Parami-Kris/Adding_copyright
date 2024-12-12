n = 5
a = list(range(1, n+1))
b = [i * i for i in a]
b_set = set(b)

YES = 0
for i in range(n):
    for j in range(n):  # Iterate over all pairs, including reverse
        if i != j and b[i] + b[j] in b_set:
            print("yes", b[i], b[j])
            YES += 1

print("Total numbers:", YES)

'''     README
find pairs of squares from a list where the sum of the squares is also a square
a = list(range(1, n+1)): Creates a list [1, 2, 3, 4, 5]
b = [i * i for i in a]: Creates a list of squares [1, 4, 9, 16, 25]
We iterate over all pairs (b[i], b[j]) where i != j.
Condition: Check if the sum of two squares (b[i] + b[j]) exists in b_set.
Output: Prints the total count of valid pairs.'''
