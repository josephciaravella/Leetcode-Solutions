def combinationSum(nums, target):
    res = []

    def backtrack(start, path, curr_sum):
        if curr_sum == target:
            res.append(path.copy())
            return
        if curr_sum > target:
            return


        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i, path, curr_sum + nums[i])
            path.pop()

    backtrack(0, [], 0)        
    return res