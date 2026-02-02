def rob(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    dp = [nums[0], max(nums[0], nums[1])]

    for i in range(2, len(nums)):
        val = max(dp[i-1], nums[i] + dp[i-2])
        dp.append(val)

    return dp[-1]

rob([5,1,2,10,6,2,7,9,3,1])