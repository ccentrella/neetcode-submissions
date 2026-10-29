class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return max_profit