def lengthOfLIS(nums):
    if not nums:
        return 0

    tab = [1] * len(nums)
    longest = 1

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                tab[i] = max(tab[i], tab[j] + 1)
        longest = max(longest, tab[i])

    return longest

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([0,1,0,3,2,3]))