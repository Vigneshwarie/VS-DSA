
def letter_case_transform(input, idx_subproblem, partial_solution):
    if idx_subproblem == len(input):
        print(partial_solution)
        return

    if input[idx_subproblem].isdigit():
        letter_case_transform(input, idx_subproblem+1,
                              partial_solution+input[idx_subproblem])
    else:
        letter_case_transform(input, idx_subproblem+1,
                              partial_solution+input[idx_subproblem].lower())
        letter_case_transform(input, idx_subproblem+1,
                              partial_solution+input[idx_subproblem].upper())


# To print it one by one
print("Printing the output as list...")
input = "a1b1C4bbR"
letter_case_transform(input, 0, "")


def letter_case_transform_list(input, idx_subproblem, partial_solution, final_list):
    if idx_subproblem == len(input):
        final_list.append(partial_solution)
        return

    if input[idx_subproblem].isdigit():
        letter_case_transform_list(input, idx_subproblem+1,
                                   partial_solution+input[idx_subproblem], final_list)
    else:
        letter_case_transform_list(input, idx_subproblem+1,
                                   partial_solution+input[idx_subproblem].lower(), final_list)
        letter_case_transform_list(input, idx_subproblem+1,
                                   partial_solution+input[idx_subproblem].upper(), final_list)


def print_letter_case_transform_list(input):
    final_list = []
    letter_case_transform_list(input, 0, "", final_list)
    return final_list


print("\n")
print("Printing the output in an array...")
# To print it as list
input = "a1b1C4bbR"
answer = print_letter_case_transform_list(input)
print(answer)
