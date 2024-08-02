# Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.

# Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for .

# This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors(albeit different from ones used in this problem).


def dutch_national_flag_problem(arr):
    left, mid, right = 0, 0, len(arr) - 1
    while mid <= right:
        if arr[mid] == 'R':
            arr[left], arr[mid] = arr[mid], arr[left]
            mid = mid + 1
            left = left + 1
        elif arr[mid] == 'G':
            mid = mid + 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right = right - 1
    return arr


arr = ["G", "B", "G", "G", "R", "B", "R", "G"]
print(dutch_national_flag_problem(arr))
