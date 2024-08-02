# Intersection Of Three Sorted Arrays
# Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

'''
Input: {
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}

Output: [2, 10]
If the intersection is empty, return an array with one element -1.
'''


def intersection_three_sorted_arrays(arr1, arr2, arr3):
    i, j, k, x = 0, 0, 0, 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            x = arr1[i]
            result.append(arr1[i])
            if i < len(arr1) and x == arr1[i]:
                i = i+1
            if j < len(arr2) and x == arr2[j]:
                j = j+1
            if k < len(arr3) and x == arr3[k]:
                k = k+1

        elif arr1[i] < arr2[j] or arr1[i] < arr3[k]:
            i = i+1
        elif arr2[j] < arr3[k]:
            j = j+1
        else:
            k = k+1

    if len(result) == 0:
        return [-1]
    else:
        return result


arr1 = [1, 2, 2, 2, 9]
arr2 = [1, 1, 2, 2]
arr3 = [1, 1, 1, 2, 2, 2]
print(intersection_three_sorted_arrays(arr1, arr2, arr3))
