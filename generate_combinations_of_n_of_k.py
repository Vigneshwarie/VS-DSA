# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]

# Problem No. 77

def generate_combinations(n, k, index_subproblem, partial_solution, final_result):
    if len(partial_solution) == k:
        final_result.append(partial_solution.copy())
        return

    if index_subproblem == n:
        return

    partial_solution.append(index_subproblem+1)
    generate_combinations(n, k, index_subproblem+1,
                          partial_solution, final_result)
    partial_solution.pop()

    generate_combinations(n, k, index_subproblem+1,
                          partial_solution, final_result)


n = 6
k = 3
final_result = []
generate_combinations(n, k, 0, [], final_result)
print("Final Result:", final_result)
