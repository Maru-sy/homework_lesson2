import random
numbers = []
number_count = 0
unique_numbers_list = []
for i in range(10):
    numbers.append(random.randint(0, 10))
print(numbers)
print(set(numbers))
for i in range(10):
    number_count = numbers.count(numbers[i])
    if number_count == 1:
        unique_numbers_list.append(numbers[i])
print(unique_numbers_list)

first_list = []
second_list = []
number_count_list1 = 0
number_count_list2 = 0
first_list_unique_nums = []
second_list_unique_nums = []
for i in range(10):
    first_list.append(random.randint(0, 20))
    second_list.append(random.randint(0, 20))
print(first_list)
print(second_list)
for i in range(10):
    number_count_list1 = first_list.count(first_list[i])
    if number_count_list1 == 1:
        first_list_unique_nums.append(first_list[i])
print(first_list_unique_nums)
for i in range(10):
    number_count_list2 = second_list.count(second_list[i])
    if number_count_list2 ==1:
        second_list_unique_nums.append(second_list[i])
print(second_list_unique_nums)
unique_numbers_list1 = set(first_list_unique_nums)
unique_numbers_list2 = set(second_list_unique_nums)
unique_numbers_both_lists = unique_numbers_list1.intersection(unique_numbers_list2)
print(unique_numbers_both_lists)



