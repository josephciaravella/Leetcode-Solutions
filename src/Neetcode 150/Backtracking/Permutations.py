def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for num in nums:
            if num in path:
                continue

            path.append(num)
            backtrack(path)
            path.pop()  # Backtracking Step

    backtrack([])
    return res