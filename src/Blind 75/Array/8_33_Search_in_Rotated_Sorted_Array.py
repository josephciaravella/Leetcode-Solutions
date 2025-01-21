def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left_ind = 0
    right_ind = len(nums) - 1
    

    while (left_ind <= right_ind):
        midpt = (left_ind + right_ind) // 2

        if (target == nums[midpt]):
            return midpt

        if nums[left_ind] <= nums[midpt]:
            if target > nums[midpt] or target < nums[left_ind]:
                left_ind = midpt + 1
            else:
                right_ind = midpt - 1
        
        else:
            if target < nums[midpt] or target > nums[right_ind]:
                right_ind = midpt - 1
            else:
                left_ind = midpt + 1

    return -1 

def search2(nums, target):
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    def findMinInd(nums):
        l, r = 0, len(nums)-1 

        while l < r:
            mid = (l+r)//2
            if r-l == 1:
                if nums[l] < nums[r]:
                    return l
                else: 
                    return r
            if nums[mid] < nums[r]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid

    min_ind = findMinInd(nums)
    if target > nums[-1]:
        l, r  = 0, min_ind-1
    else:
        l, r = min_ind, len(nums)-1

    if nums[l] == target or nums[r] == target:
        return l if nums[l] == target else r

    while l < r:
        mid = (l+r)//2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            r = mid-1
        elif nums[mid] > target:
            l = mid+1

    return -1

        
print(search2([4,5,6,7,0,1,2], 0))