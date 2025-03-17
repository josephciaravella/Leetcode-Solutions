def jump(nums):
    if not nums or len(nums) == 1:
        return 0
    steps = 0
    curr_reach = 0
    next_reach = 0
    for i in range(len(nums)-1):
        next_reach = max(next_reach, i+nums[i])
        if i == curr_reach:
            curr_reach = next_reach
            steps += 1

            if curr_reach >= len(nums)-1:
                return steps

    return steps

jump([1,2])