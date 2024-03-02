

def list_numbers_mult(numbers_list: list, nums_multiplied: 1):
    for i in range(len(numbers_list)):
        nums_multiplied *= numbers_list[i]
    return nums_multiplied


try:
    print(f"Result of list numbers multiplication: \
    {list_numbers_mult([1, 2, 3, 4, 6], 1)}")
except Exception as e:
    print(e)


def list_numbers_minimum(numbers_list: list):
    return min(numbers_list)


try:
    print(f"The minimal number in the list: {list_numbers_minimum([1, 2, 3, 4, 2, 1, -2])}")
except Exception as e:
    print(e)


def prime_numbers_counter(numbers_list: list, prime_nums_count: int, is_prime: bool):
    for nums in numbers_list:
        is_prime = True
        if nums < 2:
            is_prime = False
        if nums > 2:
            for i in range(2, nums):
                if nums % i == 0:
                    is_prime = False
        if is_prime:
            prime_nums_count += 1
    return prime_nums_count


try:
    print(f"There are {prime_numbers_counter([1, 2, 4, 5, 6, 7, 8, 9, 10, 7],
      0, True)} prime numbers in the list")
except Exception as e:
    print(e)


def removed_nums_counter(numbers_list: list, num_to_remove: int, removed_nums_count: int):
    import copy
    list_after_removal = numbers_list.copy()
    while num_to_remove in list_after_removal:
        list_after_removal.remove(num_to_remove)
    removed_nums_count = len(numbers_list) - len(list_after_removal)
    return removed_nums_count


try:
    number_to_remove = 3
    print(f"Number {number_to_remove} was removed {removed_nums_counter
    ([1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 3], number_to_remove, 0)} times")
except Exception as e:
    print(e)


def list_of_lists(first_list: list, second_list: list, general_list: list):
    general_list.extend(first_list)
    general_list.extend(second_list)
    return general_list


try:
    print(list_of_lists([1, 2, 3], [3, 2, 1, 4, 5], []))
except Exception as e:
    print(e)


def raise_elements_to_power(numbers_list: list, power: int):
    for i in range(len(numbers_list)):
        numbers_list[i] = numbers_list[i] ** power
    return numbers_list


try:
    print(raise_elements_to_power([1, 2, 3, 4, 1], 3))
except Exception as e:
    print(e)






























