import time


def fibonacci_recursion(n):
    seq = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


# print("\n")
# print(f"Start time : {time.time()} seconds")
# print([fibonacci_recursion(n) for n in range(35)])
# print(f"End time : {time.time()} seconds")


def fibonacci_optimized(n, a1, a2):
    if n == 0:
        return a1
    else:
        return fibonacci_optimized(n-1, a2, a1+a2)


print("\n")
print(f"Start time : {time.time()} seconds")
print([fibonacci_optimized(n, 0, 1) for n in range(30)])
print(f"End time : {time.time()} seconds")


def fibonacci_bottomup_dynamic(n):
    a1, a2 = 0, 1
    for _ in range(n):
        a1, a2 = a2, a1+a2

    return a1


print("\n")
print(f"Start time : {time.time()} seconds")
print([fibonacci_bottomup_dynamic(n) for n in range(30)])
print(f"End time : {time.time()} seconds")
