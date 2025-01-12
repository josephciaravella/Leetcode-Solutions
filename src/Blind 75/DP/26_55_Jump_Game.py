def canJumpBottomUp(nums):
    dp = [False] * len(nums)
    dp[0] = True
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    for i, num in enumerate(nums):
        if i == len(nums)-1:
            return False
        if num > 0:
            for j in range(1, num+1):
                if not dp[i+j]:
                    dp[i+j] = True
                    if i+j == len(nums)-1:
                        return dp[-1]
                else: 
                    continue
        elif dp[i+1]:
            continue
        else:
            return False

print(canJumpBottomUp([3,0,8,2,0,0,1])) # False

# OPTIMAL SOLUTION
def canJumpTopDown(nums):
    target = len(nums)-1
    for i in range(target-1, -1, -1):
        if i + nums[i] >= target:
            target = i
    return target <= 0