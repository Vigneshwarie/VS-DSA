# Brute Force Algorithm - Bubble Sort
# Compare each pair of adjacent elements in the list and swap them if they are in the wrong order


import time


def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


numbers = [6, 4, 9, 27, 10, 2, 8, 20, 10, 7, 5, 3, 12, 13,
           14, 15, 16, 17, 18, 19, 11, 20, 21, 22, 24, 25, 26, 23]

print(f"Start time : {time.time()} seconds")
print(bubble_sort(numbers))
print(f"End time : {time.time()} seconds")
