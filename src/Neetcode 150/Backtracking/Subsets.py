class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            # reached the end of the path
            if index == len(nums):
                result.append(path[:])
                return

            # decision: take number
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()  # Backtracking Step

            # decision: dont take number
            backtrack(index+1, path)

        backtrack(0, [])
        return result