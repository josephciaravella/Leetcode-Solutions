def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = {}
    for i in range(len(nums)):
        hashtable[nums[i]] = i
    
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in hashtable and hashtable[rem] != i :
            return [i, hashtable[rem]]