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
