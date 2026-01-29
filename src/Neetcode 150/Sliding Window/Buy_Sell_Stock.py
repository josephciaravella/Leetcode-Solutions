class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        pft = 0
        
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            pft = max(pft, prices[i]-curr_min)

        return pft