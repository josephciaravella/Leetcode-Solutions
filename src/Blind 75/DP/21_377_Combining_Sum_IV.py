def combinationSum4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # [3,4,5,7] -> 12
    # i = 1 -> dp[i] = 0
    # i = 2 -> dp[i] = 0
    # i = 3 -> dp[i] = 1
    # i = 4 -> dp[i] = 1
    # i = 5 -> dp[i] = 1
    # i = 6 -> +1 for 3, dp[i] = 1
    # i = 7 -> +1 for 3, +1 for 4, +1 for 7 dp[i] = 3
    # i = 8 -> +1 for 3, +1 for 4, +1 for 5, dp[i] = 3
    # i = 9 -> +1 for 3, +1 for 4, +1 for 5, dp[i] = 3
    # i = 10 -> +3 for 3, +1 for 5, +1 for 7, dp[i] = 5
    # i = 11 -> +3 for 3, +3 for 4, +1 for 5, +1 for 7, dp[i] = 8
    # i = 12 -> +3 for 3, +3 for 4, +3 for 5, +1 for 7, dp[i] = 10



    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if (i - num >= 0):
                dp[i] += dp[i - num]
    
    return dp[-1]