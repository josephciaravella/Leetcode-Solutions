def maxSubArray(nums):
    #griddy
    curr_sum = 0
    max_sum = nums[0]

    for num in nums:
        if curr_sum + num > num:
            curr_sum += num
        else:
            curr_sum = num
        
        if max_sum < curr_sum:
            max_sum = curr_sum

    return max_sum