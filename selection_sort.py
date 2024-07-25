# Brute Force Algorithm
# Select the smallest element from the list and swap it with the first element and repeat the process
# Time Complexity: O(n^2)
# Space Complexity: O(1)
import time


def selection_sort(numbers):
    for i in range(len(numbers)):
        minIndex = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[minIndex]:
                minIndex = j
        numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
    return numbers


numbers = [6, 4, 9, 10, 2, 8, 20, 10, 7, 5, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
           31, 32, 33, 34, 35, 36, 37, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 38, 39, 40, 41, 28, 29, 30]
print(f"Start time : {time.time()} seconds")
print(selection_sort(numbers))
print(f"End time : {time.time()} seconds")
