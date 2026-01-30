def subsetsWithDup(nums):
    res = []
    nums = sorted(nums)
    def backtrack(start, path):            
        # track the current path
        res.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue

            # take the number
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()  # Backtracking Step

    backtrack(0, [])
    return res