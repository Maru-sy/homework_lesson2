def my_pow(number, power):
    if power <= 1:
        return number

    return number * my_pow(number, power - 1)


print(my_pow(2, 4))

#my_pow(2,4) -> 2 * my_pow(2,3) => 16
#my_pow(2,3) -> 2 * my_pow(2,2) => 8
#my_pow(2,2) -> 2 * my_pow(2,1) => 4
#my_pow(2,1) => 2


def asterisk(number):
    if number <= 1:
        return "*"

    return "*" + str(asterisk(number - 1))


print(asterisk(5))

#asterisk(5) -> "*" + str(asterisk(4) => "*****"
#asterisk(4) -> "*" + str(asterisk(3) => "****"
#asterisk(3) -> "*" + str(asterisk(2) => "***"
#asterisk(2) -> "*" + str(asterisk(1) => "**"
#asterisk(1) -> "*"

#если диапазон от start_number до finish_number включительно


def numbers_sum(start_number: int, finish_number: int):
    if finish_number <= start_number:
        return start_number

    return finish_number + numbers_sum(start_number, finish_number - 1)


print(numbers_sum(20, 23))


#numbers_sum(20,23) -> 23 + numbers_sum(20,22) => 86
#numbers_sum(20,22) -> 22 + numbers_sum(20,21) => 63
#numbers_sum(20,21) -> 21 + numbers_sum(20,20) => 41
#number_sum(20,20)  -> start_number => 20


#я создала отдельный список для сумм sum_list и по очереди их добавила в него,
#потом нашла индекс минимальной суммы в списке sum_list
#он совпадает с индексом начального элемента минимальной суммы в основном списке nums_list


def minimal_sum_index_search(nums_list: list, sum_list: list, start_index, finish_index):
    if finish_index > len(nums_list):
        minimal_sum_index = sum_list.index(min(sum_list))
        return minimal_sum_index
    nums_sum = sum(nums_list[start_index:finish_index])
    sum_list.append(nums_sum)
    return minimal_sum_index_search(nums_list, sum_list, start_index + 1, finish_index + 1)


# print(minimal_sum_index_search([1, 2, 3, 4, 5, 6, 0, 0, 0, 7, 8, 9, 10, 0, 1, 0], [], 0, 3))


import random
numbers_list = [random.randint(0, 10) for _ in range(100)]
print(numbers_list)

print(minimal_sum_index_search(numbers_list, [], 0, 10))
