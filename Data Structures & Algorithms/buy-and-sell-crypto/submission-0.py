class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        B , S= 0 , 1

        while S < len(prices):
            if prices[B] < prices[S]:
                profit = prices[S] - prices[B]
                maxP = max(maxP, profit)
            else:
                B = S
            #Expand horizon if you can find a better sell day
            S+=1 
        return maxP
