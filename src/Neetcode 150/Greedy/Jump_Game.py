def canJump(nums) -> bool:
    dist = 0
    for i in range(len(nums)):
        if i > dist:
            return False
        else:
            dist = max(dist, i + nums[i])

    return True