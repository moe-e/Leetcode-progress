class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        
        l = 0
        r = 1
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r+= 1
            
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
                
            
        return res
        