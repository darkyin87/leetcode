matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vector = [
    1, 2, 3
]

def inner_product(row, vector):
    sum = 0
    for index, item in enumerate(row):
        sum += item * vector[index]
    return sum

def matrix_vector_product(matrix, vector):
    return [inner_product(row, vector) for row in matrix]

print matrix_vector_product(matrix, vector)
