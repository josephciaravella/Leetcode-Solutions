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