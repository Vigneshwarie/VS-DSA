

def find_three_summation(arr):
    arr.sort()
    result = []
    n = len(arr)

    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left, right = i+1, n-1
        while left < right:
            sum = arr[left] + arr[i] + arr[right]
            if sum == 0:
                result.append(f"{arr[left]},{arr[i]},{arr[right]}")
                while left < right and arr[left] == arr[left+1]:
                    left = left+1

                while left < right and arr[right] == arr[right-1]:
                    right = right-1
                left = left+1
                right = right-1
            elif sum < 0:
                left = left+1
            else:
                right = right-1
    return result


arr = [-1, 0, 1, 2, 2, -1, -4]
print(find_three_summation(arr))
