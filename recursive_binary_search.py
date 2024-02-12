# Recursive Binary Search on a array of numbers
# The function will accept an array and the value that is to be found
# The function will output the index of the number if found else return -1

def recursive_binary_search(array, low, high, val):
    middle_val = (low + high) // 2
    if high >= low:
        if array[middle_val] == val:
            return middle_val
        elif array[middle_val] > val:
            return recursive_binary_search(array, low, middle_val-1, val)
        elif array[middle_val] < val:
            return recursive_binary_search(array, middle_val+1, high, val)
    else:
        return -1


array = [3, 6, 10, 30, 45, 50, 70]
val = 10

output = recursive_binary_search(array, 0, len(array)-1, val)
print(output)
