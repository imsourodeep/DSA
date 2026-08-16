# Last updated: 16/08/2026, 12:32:56
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        i = 0
        total =0
        while i<len(discounts) and i<len(prices):
            price = prices[i]
            discount = discounts[i]
            dp = price*(100-discount)/100
            total += dp
            i+=1
        total += sum(prices[i:])
        return total
        