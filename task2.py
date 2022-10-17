def get_max_pair_sum(numbers: list) -> float:
    new_list = []
    for i in range(0, len(numbers)):
        if i != numbers[-1]:
            new_list.append(numbers[i]+numbers[i+1])
    return max(new_list)


def get_max_pair_sum2(numbers: list) -> float:
    max_pair_sum = 0
    for i, elem in enumerate(numbers[:-1]):
        elem_and_number_to_add = elem + numbers[i+1]
        print(i, elem, i+1, numbers[i+1])
        if max_pair_sum < elem_and_number_to_add:
            max_pair_sum = elem_and_number_to_add
        print(elem + numbers[i+1])
    return max_pair_sum


my_list = [5, 1, 7, 3, 4]

print(get_max_pair_sum2(my_list))
