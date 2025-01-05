import math


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left_ind = 0
    right_ind = len(nums) - 1
    

    while (left_ind <= right_ind):
        midpt = (left_ind + right_ind) // 2

        if (target == nums[midpt]):
            return midpt

        if nums[left_ind] <= nums[midpt]:
            if target > nums[midpt] or target < nums[left_ind]:
                left_ind = midpt + 1
            else:
                right_ind = midpt - 1
        
        else:
            if target < nums[midpt] or target > nums[right_ind]:
                right_ind = midpt - 1
            else:
                left_ind = midpt + 1

    return -1 


    
# print(search([4,5,6,7,0,1,2], 0))
# print(search([4,5,6,7,0,1,2], 3))
# print(search([4,5,6,7,0,1,2], 5))
# print(search([0,1,2,4,5,6,7], 5))
# print(search([1], 1))
# print(search([1,3], 0))


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
                if (r < len(nums)-1):
                    if(nums[l-1] == nums[l] or nums[r+1] == nums[r]):
                        l+=1
                        r-=1
                        continue
                if (nums[l] + nums[r] == target):
                    final.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                elif (nums[l] + nums[r] < target):
                    l+=1
                else:
                    r-=1
                
        return final

# print(threeSum([-2,0,0,2,2]))

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        area = 0
        while (l<r):
            h = min(height[l],height[r])
            area = max(area, h*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return area

# print(maxArea([1,8,6,2,5,4,8,3,7]))

def hammingWeight(n):
    count = 0
    while (n > 0):
        if (n & 1 == 1):
            count += 1
        n = n >> 1
    return count

# print(hammingWeight(128))

def missingNumber(nums):
    length = len(nums) #last num in the array
    out = length
    for i in range(0, length):
        if (nums[i] & out == out):
            out -= 1
    
    return out

# print(missingNumber([1,2]))

def coinChange(coins, amount):
        tab = [len(coins)+1] * (amount+2)
        for coin in coins:
            if (coin == amount):
                return 1
            tab[coin] = 1

        i = 1
        while (i <= amount):
            if (i in coins):
                i += 1
                continue
            for coin in coins:
                if (tab[i-coin] > 0):
                    tab[i] = min(tab[i-coin] + 1, tab[i])
                else:
                    tab[i] = 0
            i +=1

        if (tab[amount] == 0):
            return -1
        else:
            return tab[amount]
        
# print(coinChange([1], 0))

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

# print(lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(lengthOfLIS([4,10,4,3,8,9]))
# print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
# print(lengthOfLIS([0,1,0,3,2,3]))

def rob(nums):
    dp = [0, nums[0]]

    for i in range(2,len(nums)+1):
        dp.append(max(dp[i-2]+nums[i-1], dp[i-1]))
    
    return dp[-1]

# print(rob([2,7,9,3,1]))

def rob2(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    length = len(nums)
    
    # first house to 2nd to last house
    dp1 = [0]*length
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])

    # Second house to last house
    dp2 = [0]*length
    dp2[1] = nums[1]
    dp2[2] = max(nums[1], nums[2])
    

    for i in range(2, length-1):
        dp1[i] = (max(dp1[i-2]+nums[i], dp1[i-1]))
    for i in range(3, length):
        dp2[i] = (max(dp2[i-2]+nums[i], dp2[i-1]))
    
    return max(dp1[length-2], dp2[length-1])

# print(rob2([1,2,3,1]))

def uniquePaths(m, n):
    tab = [1] * (m*n)
    # instead of a 2D array with rows and cols, flatten it and iterate thru with + n
    for i in range(1,m*n):
        if (i-n) < 0 or i % n == 0:
            continue
        else:
            tab[i] = tab[i-n] + tab[i-1]

    return tab[-1]

# print(uniquePaths(3,7))

def canJumpBottomUp(nums):
    dp = [False] * len(nums)
    dp[0] = True
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    for i, num in enumerate(nums):
        if i == len(nums)-1:
            return False
        if num > 0:
            for j in range(1, num+1):
                if not dp[i+j]:
                    dp[i+j] = True
                    if i+j == len(nums)-1:
                        return dp[-1]
                else: 
                    continue
        elif dp[i+1]:
            continue
        else:
            return False

print(canJumpBottomUp([3,0,8,2,0,0,1])) # False

# OPTIMAL SOLUTION
def canJumpTopDown(nums):
    target = len(nums)-1
    for i in range(target-1, -1, -1):
        if i + nums[i] >= target:
            target = i
        return target <= 0
