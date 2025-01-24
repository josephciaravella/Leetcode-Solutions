def missingNumber(nums):
    length = len(nums)
    out = 0
    theoretical = length*(length+1)//2
    for i in range(0, length):
        out += nums[i]
    
    return theoretical-out

print(missingNumber([1,2]))