def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp_max = nums[0]
    temp_min = nums[0]
    product = temp_max

    for i in range(1, len(nums)):
        num = nums[i]
        temp = max(num, temp_max*num, temp_min*num)
        temp_min = min(num, temp_max*num, temp_min*num)
        temp_max = temp
        if temp_max > product:
            product = temp_max
    
    return product
    