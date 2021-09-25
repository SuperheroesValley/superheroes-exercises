class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            current_profit = price - min_price
            if current_profit > 0 and current_profit > max_profit:
                max_profit = current_profit
            if price < min_price:
                min_price = price
        return max_profit
