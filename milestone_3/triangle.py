# Description: This function creates a Pascal's triangle of a given number of rows
def get_triangle(rows: int) -> list[list[int]]:
    triangle = [[1]*(i+1) for i in range(rows)]
    for i in range(rows):
        for j in range(1,i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

# This function prints the Pascal's triangle in simple way
def print_triangle_simple(triangle: list[list[int]]) -> None:
    for row in triangle:
        print(row)

# This function prints the Pascal's triangle in a centered way
def print_triangle_center(triangle: list[list[int]]) -> None:
    for row in triangle:
        print(" ".join(str(i) for i in row).center(100))

# Test
# print_triangle_simple(get_triangle(5))
# print_triangle_center(get_triangle(5))

# Input from user and print the Pascal's triangle
rows = int(input("Enter the number of rows for the Pascal's triangle: "))
print_triangle_center(get_triangle(rows))