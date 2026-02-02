def minCostClimbingStairs(cost) -> int:
    if len(cost) == 2:
        return min(cost[0], cost[1])

    dp = [cost[0], cost[1]]

    for i in range(2, len(cost)):
        val = min(dp[i-1], dp[i-2]) + cost[i]
        dp.append(val)

    return min(dp[-1], dp[-2])

print(minCostClimbingStairs([1,2,3]))