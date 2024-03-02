# 5. Task: Matrix Multiplication
# Write a function to perform matrix multiplication of two matrices without using any external libraries.
# Solution: Write a function that performs matrix multiplication by iterating through the matrices and calculating the dot product of corresponding elements.


def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        print("Cannot multiply matrices. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
matrix1 = []
for i in range(rows1):
    # row = []
    for j in range(cols1):
        element = int(input(f"Enter element at position ({i+1}, {j+1}) of the first matrix: "))
        # row.append(element)
        matrix1.append(element)

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
matrix2 = []
for i in range(rows2):
    row = []
    for j in range(cols2):
        element = int(input(f"Enter element at position ({i+1}, {j+1}) of the second matrix: "))
        row.append(element)
    matrix2.append(row)

# Displaying the user-defined matrices
print("First matrix:")
for row in matrix1:
    print(row)

print("Second matrix:")
for row in matrix2:
    print(row)

result = multiply_matrices(matrix1, matrix2)
if result:
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
