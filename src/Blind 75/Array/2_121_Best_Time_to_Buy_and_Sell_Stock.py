def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    curr_min = 10001

    for i in range(len(prices)):
        profit = max(profit, prices[i]-curr_min)
        curr_min = min(prices[i], curr_min)

    return profit