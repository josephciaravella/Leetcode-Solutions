def letterCombinations(digits: str):
    nums = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8': "tuv", '9':"wxyz"}
    res = []

    def backtrack(start, combo):
        # base case
        if len(digits) == start:
            res.append(combo)
            return
        # iterate through choices
        for char in nums[digits[start]]:
            backtrack(start+1, combo+char)

    if digits:
        backtrack(0, "")
    return res

print(letterCombinations("34"))