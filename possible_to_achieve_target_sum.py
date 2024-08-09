def sum_helper(arr, k, index_subproblem, partial_solution):
    if partial_solution == k:
        return True

    if index_subproblem == len(arr):
        return False

    if sum_helper(arr, k, index_subproblem+1,
                  partial_solution):
        return True

    if sum_helper(arr, k, index_subproblem+1,
                  partial_solution+arr[index_subproblem]):
        return True

    return False


def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    index_subproblem = 0
    partial_solution = 0
    result = sum_helper(arr, k, index_subproblem, partial_solution)
    return result


arr = [1, 2, 3, -4, -6, 4, 5, 10]
output = check_if_sum_possible(arr, 30)
print("output===", output)
