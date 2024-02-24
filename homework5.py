try:
    # numbers = [1, 4, -6, 9, -8, 10, 12, 7, 3, 9]
    even_numbers_total = 0
    odd_numbers_total = 0
    negative_numbers_total = 0
    index_intdiv3_multiplication = 1
    elements_total = 0
    numbers = []
    NUM_SIZE = int(input("Enter the length of list: "))
    import random
    for i in range(NUM_SIZE):
        numbers.append(random.randint(-10, 10))
    print(numbers)
    for i in range(NUM_SIZE):
        if numbers[i] % 2 == 0 and numbers[i] != 0:
            even_numbers_total += numbers[i]
    print(f"Even numbers sum: {even_numbers_total}")
    for i in range(NUM_SIZE):
        if numbers[i] % 2 != 0:
            odd_numbers_total += numbers[i]
    print(f"Odd numbers sum: {odd_numbers_total}")
    for i in range(NUM_SIZE):
        if numbers[i] < 0:
            negative_numbers_total += numbers[i]
    print(f"Negative numbers sum: {negative_numbers_total}")
    for i in range(NUM_SIZE):
        if i % 3 == 0:
            index_intdiv3_multiplication *= numbers[i]
    print(f"Multiplication of numbers with index%3=0: {index_intdiv3_multiplication}")
    min_number = min(numbers)
    max_number = max(numbers)
    print(f"Minimal and maximal number multiplication: {min_number * max_number}")
    for i in range(NUM_SIZE):
        if numbers[i] > 0:
            last_positive_number_index = i
    for i in range(NUM_SIZE - 1, -1, -1):
        if numbers[i] > 0:
            first_positive_number_index = i
    print(first_positive_number_index, last_positive_number_index)
    for i in range(first_positive_number_index + 1, last_positive_number_index):
        elements_total += numbers[i]
    print(f"Between first and last positive number elements sum: {elements_total}")
except Exception as e:
    print(e)
try:
    numbers2 = []
    import random
    NUM_SIZE2 = int(input("Enter size of a list: "))
    for i in range(NUM_SIZE2):
        numbers2.append(random.randint(-10, 10))
    print(numbers2)
    nums2_even = []
    nums2_odd = []
    nums2_positive = []
    nums2_negative = []
    for i in range(NUM_SIZE2):
        if numbers2[i] % 2 == 0 and numbers2[i] != 0:
            nums2_even.append(numbers2[i])
        if numbers2[i] % 2 != 0:
            nums2_odd.append(numbers2[i])
        if numbers2[i] > 0:
            nums2_positive.append(numbers2[i])
        if numbers2[i] < 0:
            nums2_negative.append(numbers2[i])
    print(f"Even numbers: {nums2_even}")
    print(f"Odd numbers: {nums2_odd}")
    print(f"Positive numbers: {nums2_positive}")
    print(f"Negative numbers: {nums2_negative}")
except Exception as e:
    print(e)

