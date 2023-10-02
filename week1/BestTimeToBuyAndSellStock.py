class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # given array prices where prices[i] is price of given day


        # buy low, sell high
        # left = buy
        # right = sell

        # if left ever becomes lower than right, update left to be right

        l = 0 
        r = 1
        res = 0

        while r < len(prices):

            if prices[l] > prices[r]:
                l = r 
                r+=1
            else:
                dif = prices[r] - prices[l]
                res = max(dif, res)
                r+=1

        return res