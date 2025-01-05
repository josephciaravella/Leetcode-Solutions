def rob2(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    length = len(nums)
    
    # first house to 2nd to last house
    dp1 = [0]*length
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])

    # Second house to last house
    dp2 = [0]*length
    dp2[1] = nums[1]
    dp2[2] = max(nums[1], nums[2])
    

    for i in range(2, length-1):
        dp1[i] = (max(dp1[i-2]+nums[i], dp1[i-1]))
    for i in range(3, length):
        dp2[i] = (max(dp2[i-2]+nums[i], dp2[i-1]))
    
    return max(dp1[length-2], dp2[length-1])

print(rob2([1,2,3,1]))