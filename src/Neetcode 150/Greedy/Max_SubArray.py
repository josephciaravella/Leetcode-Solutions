def maxSubArray(nums) -> int:
    out = nums[0]
    sub = []
    for i in range(len(nums)):
        if nums[i] > sum(sub)+nums[i]:
            sub = []

        out = max(out, sum(sub)+nums[i])
        sub.append(nums[i])    
        

    return out

maxSubArray([2,-3,4,-2,2,1,-1,4])