class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # move the pointer so we don't keep adding the same triplet
                    l += 1
                    # make sure l is in range
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1


        return res