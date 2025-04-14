def maxProduct(nums):
    NUMS = len(nums)
    max_prod = [0] * NUMS
    min_prod = [0] * NUMS
    global_max = nums[0]

    max_prod[0] = nums[0]
    min_prod[0] = nums[0]
    for i in range(1, NUMS):
        max_prod[i] = max(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
        min_prod[i] = min(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])

        global_max = max(global_max, max_prod[i])

    
    return global_max

# can also just use a variable, do not need an array