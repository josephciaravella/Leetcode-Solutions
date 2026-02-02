import math, heapq
def kClosest(points, k: int):
    heap = []

    for point in points:
        x, y = point
        d = math.sqrt(x**2 + y**2)
        heap.append((d, x, y))

    heapq.heapify(heap)
    res = []
    for _ in range(k):
        root = heapq.heappop(heap)
        res.append([root[1], root[2]])
    
    return res

kClosest([[3,3],[5,-1],[-2,4]], 2)