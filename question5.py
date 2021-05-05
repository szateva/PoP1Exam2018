""" Given an integer n, produce a two-dimensional array of size (n x n) and set each value
according to the following rules:
• On the main diagonal set the value to 0.
• On the diagonals adjacent to the main diagonal, set the value to 1.
• On the next adjacent diagonals set the value to 2, and so on.
You should print out the elements of the resulting array with a space between each
element and a line break at the end of each row.
For example, for n = 5, the resulting array would have the following values:
0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
You should not simply assign to each element in the array but should utilise appropriate
iteration constructs. """

def matrix(n):
    M = [[0] * n for i in range(n)]
    for row in range(n):
        for col in range(n):
            if row < col:
                M[row][col] = col - row
            elif row > col:
                M[row][col] = row - col
            else:
                M[row][col] = 0
    return M

def print_matrix(M):
    for row in M:
        print(row)

M = matrix(5)
print_matrix(M)


