import time


def find_minimum_number(numbers):
    minValue = numbers[0]
    for number in numbers:
        if number < minValue:
            minValue = number
    return minValue


numbers = [6, 4, 9, 10, 2, 8, 20, 10, 7, 5, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
           57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 200, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 880, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 359, 400, 238, 789, 33, 433, 123, 546]

# Time complexity
start_time = time.time()
min_x = find_minimum_number(numbers)
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
print(f"Minimum value: {min_x}")
