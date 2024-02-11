# Binary Search on a reserved array

def binary_string_search(arr, search_string):
    start_index = 0
    end_index = len(arr)
    mid_index = 0

    while (start_index <= end_index):
        # To get round value while dividing
        mid_index = start_index + (end_index - start_index) // 2

        if (search_string == arr[mid_index]):
            return mid_index

        elif (search_string[0] < arr[mid_index][0]):
            start_index = mid_index + 1

        else:
            end_index = mid_index - 1

    return -1


mystringarray = ["Zebra", "Spoon", "Moon", "Home", "Apple"]

print(binary_string_search(mystringarray, "Home"))
print(binary_string_search(mystringarray, "Viggy"))
print(binary_string_search(mystringarray, "Zebra"))
