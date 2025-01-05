def lengthOfLIS(nums):
    tab = [1] * len(nums)
    longest = 1
    beginning = nums[0]
    prev_ind = 0
    for i in range(1,len(nums)):
        if (nums[i] > nums[prev_ind]):
            tab[i] = tab[prev_ind] + 1
            prev_ind = i
        elif (nums[i] >= beginning):
            tab[i] = longest
        elif (nums[i] < beginning):
            beginning = nums[i]
            prev_ind = i

        longest = max(longest, tab[i])
    
    return longest

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([0,1,0,3,2,3]))