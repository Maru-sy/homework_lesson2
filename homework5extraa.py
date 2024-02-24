try:
    import random
    import copy
    matrix = []
    main_diagonal_total = 0
    secondary_diagonal = []
    for i in range(10):
        matrix.append([])
        for j in range(10):
            matrix[i].append(random.randint(10, 99))
    for i in range(10):
        for j in range(10):
            print(matrix[i][j], end=" ")
        print()
    print()


    for i in range(10):
        main_diagonal_total += matrix[i][i]
        print(matrix[i][i], end=" ")
    print()
    print(f"Main diagonal numbers total: {main_diagonal_total}")


    for i in range(10):
        secondary_diagonal.append(matrix[i][9 - i])
    print(*secondary_diagonal)
    print(f"Minimal and maximal numbers of secondary diagonal: {min(secondary_diagonal)}, {max(secondary_diagonal)}")


    column_number = int(input("Enter column number: "))
    for i in range(10):
        print(matrix[i][column_number - 1])
    row_number = int(input("Enter row number: "))
    print(*matrix[row_number - 1])


    column_1 = int(input("Enter first column number: "))
    column_2 = int(input("Enter second column number: "))
    matrix_copy1 = copy.deepcopy(matrix)
    for i in range(10):
        column_1_number = matrix_copy1[i][column_1 - 1]
        column_2_number = matrix_copy1[i][column_2 - 1]
        matrix_copy1[i][column_1 - 1] = column_2_number
        matrix_copy1[i][column_2 - 1] = column_1_number
    for i in range(10):
        for j in range(10):
            print(matrix_copy1[i][j], end=" ")
        print()


    row_1 = int(input("Enter first row number: "))
    row_2 = int(input("Enter second row number: "))
    matrix_copy2 = copy.deepcopy(matrix)
    row_1_number = matrix_copy2[row_1 - 1]
    row_2_number = matrix_copy2[row_2 - 1]
    matrix_copy2[row_1 - 1] = row_2_number
    matrix_copy2[row_2 - 1] = row_1_number
    for i in range(10):
        for j in range(10):
            print(matrix_copy2[i][j], end=" ")
        print()
except Exception as e:
    print(e)