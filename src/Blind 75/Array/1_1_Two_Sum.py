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
        


def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    diff = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in diff:
            diff[num] = i
        else :
            return [i, diff[complement]]
# twoSum([3,2,4])