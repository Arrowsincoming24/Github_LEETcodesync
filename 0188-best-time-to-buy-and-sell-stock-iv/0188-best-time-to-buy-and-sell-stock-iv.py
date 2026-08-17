class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for transaction in range(1, k + 1):
                buy[transaction] = max(
                    buy[transaction],
                    sell[transaction - 1] - price
                )

                sell[transaction] = max(
                    sell[transaction],
                    buy[transaction] + price
                )

        return sell[k]
        