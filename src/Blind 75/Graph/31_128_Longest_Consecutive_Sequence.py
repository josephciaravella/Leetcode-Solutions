def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest_path = 0
    arr_entries = set(nums)
    visited = set()
    for num in nums:
        if num in visited:
            continue
        visited.add(num)
        curr_path = 0
        if num-1 not in arr_entries:
            curr_path += 1
            while num+1 in arr_entries:
                curr_path += 1
                num += 1
            if curr_path > longest_path:
                longest_path = curr_path
    
    return longest_path

print(longestConsecutive([100,4,200,1,3,2])) #4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(longestConsecutive([1,2,0,1])) # 3
print(longestConsecutive([0])) # 1
print(longestConsecutive([0,0])) # 1
print(longestConsecutive([])) # 0
