# Last updated: 05/09/2026, 12:51:07
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
        