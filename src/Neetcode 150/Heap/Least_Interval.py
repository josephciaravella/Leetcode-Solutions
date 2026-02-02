import heapq
from collections import deque, Counter
def leastInterval(tasks, n: int) -> int:
    counts = Counter(tasks)
    max_heap = [-cnt for cnt in counts.values()]
    heapq.heapify(max_heap)

    # have maxheapified sequence of tasks
    queue = deque()
    out = 0
    while max_heap or queue:
        out += 1
        if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count != 0:
                queue.append((count, out+n))

        if queue and queue[0][1] == out:
            heapq.heappush(max_heap, queue.popleft()[0])

    return out