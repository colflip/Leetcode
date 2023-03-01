from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_input = prices[0]
        max_profit = 0
        for p in prices[1:]:
            min_input = min(p, min_input)
            max_profit = max(max_profit, p - min_input)
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
