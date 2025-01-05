def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i-1]*nums[i-1]
        
        last = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            answer[i] *= last
            last *= nums[i]
            
        return answer