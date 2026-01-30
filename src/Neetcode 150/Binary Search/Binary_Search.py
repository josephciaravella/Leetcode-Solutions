def search(nums, target: int) -> int:
    mid = len(nums)//2
    l, r = 0, len(nums)-1
    while l<=r:
        val = nums[mid]
        if val > target:
            r = mid-1
        elif val < target:
            l = mid+1
        else:
            return mid
            
        mid = l + (r-l)//2

    return -1

search([-1,0,2,4,6,8], 3)