class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        f_buy=float('-inf')
        s_buy=float('-inf')
        f_sell=0
        s_sell=0

        for price in prices:
            f_buy=max(f_buy,-price)
            f_sell=max(f_sell,f_buy+price)

            s_buy=max(s_buy,f_sell-price)
            s_sell=max(s_sell,s_buy+price)
    
        return s_sell