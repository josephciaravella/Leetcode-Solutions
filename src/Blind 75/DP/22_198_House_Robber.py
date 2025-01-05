def rob(nums):
    dp = [0, nums[0]]

    for i in range(2,len(nums)+1):
        dp.append(max(dp[i-2]+nums[i-1], dp[i-1]))
    
    return dp[-1]

print(rob([2,7,9,3,1]))