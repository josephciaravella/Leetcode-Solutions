def insert2(intervals, newInterval):
    result = []
    added = False

    if newInterval[-1] < intervals[0][0]:
        return [newInterval] + intervals
    
    if newInterval[0] > intervals[-1][-1]:
        return intervals + [newInterval]
    
    for interval in intervals:

        if interval[0] < newInterval[0] and interval[-1] > newInterval[-1]:
            return intervals

        if interval[-1] < newInterval[0]:
            result.append(interval)
            continue

        if interval[0] > newInterval[-1]:
            if not added:
                result.append(newInterval)
                added = True
            result.append(interval)
            continue

        if interval[0] <= newInterval[0] and interval[-1] >= newInterval[0]:
            newInterval[0] = min(newInterval[0], interval[0])
            continue

        if interval[0] <= newInterval[-1] and interval[-1] >= newInterval[-1]:
            newInterval[-1] = max(newInterval[-1], interval[-1])
            continue

    if not result:
        return [newInterval]

    return result



print(insert2([[1,3],[4,6]], [2,5]))         # [[1,6]]
print(insert2([[1,2],[3,5],[9,10]], [6,7]))  # [[1,2],[3,5],[6,7],[9,10]]
print(insert2([[1,5]], [6,8]))               # [[1,5],[6,8]]
print(insert2([[1,3],[6,9]], [2,5]))         # [[1,5],[6,9]]
print(insert2([[0,2],[3,5],[6,8],[10,12],[13,15]], [4,7]))               # [[1,5]]






























