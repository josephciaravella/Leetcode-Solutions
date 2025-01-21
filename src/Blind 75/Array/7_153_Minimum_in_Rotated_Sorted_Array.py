def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_ind = 0
    right_ind = len(nums) - 1
    midpt = len(nums) // 2
    left = nums[left_ind]
    right = nums[right_ind]
    mid = nums[midpt]
    final_min = mid
    temp = mid

    while (left_ind != right_ind):
        if (mid > right):
            left_ind = midpt + 1
            left = nums[left_ind]
        
        elif (mid < right):
            # do same but for left
            right_ind = midpt
            right = nums[right_ind]
        
        midpt = (left_ind + right_ind) // 2
        mid = nums[midpt]

        if (mid < final_min):
            final_min = mid
        
    return final_min


def findMin2(nums):
    l, r = 0, len(nums)-1 

    while l < r:
        mid = (l+r)//2
        if r-l == 1:
            return min(nums[l], nums[r])
        if nums[mid] < nums[r]:
            r = mid
        elif nums[l] < nums[mid]:
            l = mid
            
print(findMin2([4,5,6,7]))   