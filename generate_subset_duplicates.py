# Generate subsets of string that includes duplicate values

def generate_subset_duplicates(input_str, index_subproblem, partial_solution, final_result):
    if index_subproblem == len(input_str):
        final_result.append("".join(partial_solution))
        return

    partial_solution.append(input_str[index_subproblem])
    generate_subset_duplicates(
        input_str, index_subproblem+1, partial_solution, final_result)
    partial_solution.pop()

    while index_subproblem + 1 < len(input_str) and input_str[index_subproblem] == input_str[index_subproblem + 1]:
        index_subproblem += 1

    generate_subset_duplicates(
        input_str, index_subproblem+1, partial_solution, final_result)


input_str = "ccba"
final_result = []
generate_subset_duplicates(sorted(input_str), 0, [], final_result)

print("Final Result:", final_result)
