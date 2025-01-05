def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        final = []

        for i, val in enumerate(nums):
            target = val*-1
            l, r = i+1, len(nums)-1
            if (i > 0 and val == nums[i-1]):
                continue
            
            while(l<r):
                
                if (nums[l] + nums[r] == target):
                    final.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif (nums[l] + nums[r] < target):
                    l+=1
                else:
                    r-=1
                
        return final