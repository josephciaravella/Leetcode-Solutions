def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    
    merger = intervals[0]
    res = []
    for i in range(1, len(intervals)):
        if merger[-1] >= intervals[i][0]:
            merger[0] = min(merger[0], intervals[i][0])
            merger[-1] = max(intervals[i][-1], merger[-1])
        else:
            res.append(merger)
            merger = intervals[i]
    res.append(merger)

    return res