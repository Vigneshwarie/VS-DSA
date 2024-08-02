# Segregate all the odd and even numbers together in a given array

def segregate_odd_even(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while left < right and arr[left] % 2 == 0:
            left = left+1

        while left < right and arr[right] % 2 != 0:
            right = right-1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left = left+1
            right = right-1
    return arr


arr = [1, 2, 3, 4, 5, 6]
print(segregate_odd_even(arr))
