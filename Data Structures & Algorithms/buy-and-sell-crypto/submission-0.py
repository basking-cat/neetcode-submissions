class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers: the left one is for the minimum, and the right one is for the maximum
        l, r = 0, 1
        max_profit = 0
        min_price = prices[l] # don't even need the pointer l here because our interest is only for the minimum price (e.g. min_price = float('inf'))
        while r < len(prices):
            if prices[r] < min_price:
                l = r
                min_price = prices[r]

            profit = prices[r] - prices[l] # prices[l] can be replaced by min_price
            max_profit = max(max_profit, profit)

            r += 1
        
        return max_profit
    # time: O(n)
    # space: O(1)

# memo: when solving a problem using DP, in each step, the result of the previous step is used(it's not technically correct, but almost correct)
# there are bottom-up and top-down methods