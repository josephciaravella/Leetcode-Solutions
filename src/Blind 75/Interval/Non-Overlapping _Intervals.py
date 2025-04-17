def eraseOverlapIntervals(intervals):

    intervals.sort(key=lambda x: x[-1])
    prevEnd = float('-inf')
    count = 0

    for interval in intervals:
        if interval[0] < prevEnd:
            count += 1
        else:
            prevEnd = interval[-1]

    return count

print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])) # 2