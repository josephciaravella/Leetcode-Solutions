def combinationSum(nums, target):
    res = []
    nums = sorted(nums)
    
    def backtrack(start, path):
        for i in range(start, len(nums)):
            if sum(path) + nums[i] == target:
                path.append(nums[i])
                
                # don't add duplicates
                if path not in res:
                    res.append(path[:])
                
                # remove and keep checking
                path.pop()
            
            elif sum(path) + nums[i] < target:

                # take the number
                path.append(nums[i])
                backtrack(i, path) # try adding the same number again
                path.pop()

            else:
                return


    backtrack(0, [])
    return res

print(combinationSum([2,5,6,9], 9))