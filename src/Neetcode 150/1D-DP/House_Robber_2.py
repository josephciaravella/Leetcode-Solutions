def rob(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp1 = [nums[0], max(nums[0], nums[1])]
    dp2 = [nums[1], max(nums[1], nums[2])]

    for i in range(2, len(nums)-1):
        dp1.append(max(dp1[i-1], nums[i] + dp1[i-2]))

    for i in range(3, len(nums)):
        dp2.append(max(dp2[i-2], nums[i] + dp2[i-3]))
    
    return max(dp1[-1], dp2[-1])

print(rob([2,9,8,3,6]))