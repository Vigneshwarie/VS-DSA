# Given a list of meeting intervals where each interval consists of a start and an end time, check if a person can attend all the given meetings such that only one meeting can be attended at a time.
'''
Input : {
"intervals": [
[1, 5],
[5, 8],
[10, 15]
]
}

Output: 1
'''


def meeting_intervals(intervals):
    intervals.sort()

    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return 0

    return 1


intervals = [[1, 5], [5, 8], [10, 15]]
print(meeting_intervals(intervals))
