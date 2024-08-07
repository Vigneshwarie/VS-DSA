# Subset problem of string
def generate_subset_string(input_str, index_subproblem, partial_solution, final_result):
    if index_subproblem == len(input_str):
        r = "".join(partial_solution)
        final_result.append(r)
        return

    partial_solution.append(input_str[index_subproblem])
    generate_subset_string(input_str, index_subproblem+1,
                           partial_solution, final_result)
    partial_solution.pop()

    generate_subset_string(input_str, index_subproblem+1,
                           partial_solution, final_result)


input_str = "xy"
final_result = []
generate_subset_string(input_str, 0, [], final_result)

print("Final Result:", final_result)
