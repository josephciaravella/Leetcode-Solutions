def combinationSum2(candidates, target):
    res = []
    nums = sorted(candidates)

    def backtrack(start, path):
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            
            if sum(path) + nums[i] == target:
                path.append(nums[i])
                if path not in res:
                    res.append(path[:])
                path.pop()
            
            elif sum(path) + nums[i] < target:
                # take number
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            
            else:
                return

    backtrack(0, [])
    return res