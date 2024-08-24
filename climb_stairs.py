# Bottom-Up Dynamic Programming
def climb_stairs(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    climb = [0] * (n+1)
    climb[1] = 1
    climb[2] = 2

    for i in range(3, n+1):
        climb[i] = climb[i-1] + climb[i-2]

    return climb[n]


n = 30
print(climb_stairs(n))
