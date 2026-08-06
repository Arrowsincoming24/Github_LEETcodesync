class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        window_size = n - k

        if window_size == 0:
            return sum(cardPoints)

        total = sum(cardPoints)
        window_sum = sum(cardPoints[:window_size])
        min_window_sum = window_sum

        for right in range(window_size, n):
            window_sum += cardPoints[right]
            window_sum -= cardPoints[right - window_size]

            min_window_sum = min(min_window_sum, window_sum)

        return total - min_window_sum
        