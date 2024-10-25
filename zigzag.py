import math

class Solution:
    def convert(self, s: str, n: int) -> str:
        try:
            # Initialize a 2D matrix of empty strings
            m = [['' for i in range(math.ceil(len(s) / 2))] for j in range(n)]

            i, j, k = 0, 0, 0
            m[i][j] = s[k]  # Set the first character

            while True:
                i += 1
                k += 1
                m[i][j] = s[k]

                if abs(i - j) % (n - 1) == 0:
                    for _ in range(1, n):
                        i -= 1
                        j += 1
                        k += 1
                        m[i][j] = s[k]
        except IndexError:
            # Concatenate the result when the matrix is filled
            if len(s) > 1 and n > 1:
                s = ''
                for row in m:
                    for t in row:
                        s += t
        finally:
            return s

# Custom input
if __name__ == "__main__":
    s = input("Enter the string to convert: ")
    n = int(input("Enter the number of rows: "))
    
    solution = Solution()
    result = solution.convert(s, n)
    print("Converted string:", result)

'''
Enter the string to convert: PAYPALISHIRING
Enter the number of rows: 3
P   A   H   N
A P L S I I G 
Y   I   R
Converted string: PAHNAPLSIIGYIR
'''