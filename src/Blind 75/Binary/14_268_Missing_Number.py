def missingNumber(nums):
    length = len(nums) #last num in the array
    out = length
    for i in range(0, length):
        if (nums[i] & out == out):
            out -= 1
    
    return out

print(missingNumber([1,2]))