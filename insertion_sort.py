# Brute Force Algorithm - Insertion Sort
# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
# Insertion sort compares each element with the previous elements and places it in the correct position.
import time


def insertion_sort(numbers):
    for i in range(0, len(numbers)):
        temp = numbers[i]
        index = i-1
        while index >= 0 and numbers[index] > temp:
            numbers[index+1] = numbers[index]
            index = index - 1
        numbers[index+1] = temp
    return numbers


numbers = [6, 4, 9, 27, 10, 2, 8, 20, 10, 7, 5, 3, 12, 13, 72, 45,
           33, 23, 14, 15, 16, 17, 18, 19, 11, 20, 21, 22, 24, 25, 26, 23]

print(f"Start time : {time.time()} seconds")
print(insertion_sort(numbers))
print(f"End time : {time.time()} seconds")
