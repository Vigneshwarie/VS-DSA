# Subset problem of numbers

def generate_subset(input_arr, index_subproblem, partial_solution):
    if index_subproblem == len(input_arr):
        print(partial_solution)
        return

    partial_solution.append(input_arr[index_subproblem])
    generate_subset(input_arr, index_subproblem+1, partial_solution)
    partial_solution.pop()

    generate_subset(input_arr, index_subproblem+1, partial_solution)


input_arr = [1, 2, 3]
generate_subset(input_arr, 0, [])


