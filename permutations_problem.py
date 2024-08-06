def permutations_problem(input_arr: list[int], index_subproblem: int, partial_solution: list[int], results: list[list[int]]):
    if index_subproblem == len(input_arr):
        results.append(partial_solution)
        return

    for i in range(index_subproblem, len(input_arr)):
        input_arr[index_subproblem], input_arr[i] = input_arr[i], input_arr[index_subproblem]
        permutations_problem(input_arr, index_subproblem + 1,
                             partial_solution + [input_arr[index_subproblem]], results)
        input_arr[index_subproblem], input_arr[i] = input_arr[i], input_arr[index_subproblem]


def generate_permutations(arr: list[int]) -> list[list[int]]:
    results = []
    permutations_problem(arr, 0, [], results)
    return results


arr = [1, 2, 3]
answer = generate_permutations(arr)
print(answer)
