def jump(nums) -> int:
    if len(nums) == 1:
        return 0
    steps = 0
    dist = 0
    curr_range = 0
    for i in range(len(nums)-1):
        dist = max(dist, i+nums[i])
        if i == curr_range:
            curr_range = dist
            steps += 1

    return steps