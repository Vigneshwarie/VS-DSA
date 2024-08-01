def pair_sum_sorted_array(numbers, target):
    pair_sum = []
    selected_numbers = []
    map = {}

    for i in range(len(numbers)):
        map[numbers[i]] = i

    for i in range(len(numbers)):
        y = target - numbers[i]
        if y in map:
            if numbers[i] != y and numbers[i] not in selected_numbers and y not in selected_numbers:
                selected_numbers.append(numbers[i])
                selected_numbers.append(y)
                pair_sum.append([i, map[y]])

    if len(pair_sum) == 0:
        return [[-1, -1]]
    return pair_sum


def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    map = {}

    for i in range(0, len(numbers)):
        x = target - numbers[i]
        if numbers[i] in map:
            return [map[numbers[i]], i]
        else:
            map[x] = i

    return [-1, -1]


# print(pair_sum_sorted_array([1, 1, 1, 1], 2))
result = pair_sum_sorted_array([-100000, 100000], 0)
print(" result: ",  result)

# 1, 3, 3, 4, 6, =>6
# 1, 2 => 4
# 0, 0, 0, 0 => 0
# 1, 1, 1, 1 => 2
