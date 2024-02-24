import random
matrix = []
main_diagonal_total =0
secondary_diagonal = []
for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(random.randint(10, 99))
for i in range(10):
    for j in range(10):
        print(matrix[i][j], end= " ")
    print()
