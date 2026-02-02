import heapq
def findKthLargest(nums, k: int) -> int:
    nums = [-1*nums[i] for i in range(len(nums))]
    heapq.heapify(nums)
    for _ in range(k-1):
        heapq.heappop(nums)
    
    return -heapq.heappop(nums)

findKthLargest([2,3,1,5,4], 2)