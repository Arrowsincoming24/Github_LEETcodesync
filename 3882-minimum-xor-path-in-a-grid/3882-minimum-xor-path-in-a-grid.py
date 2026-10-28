class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        molqaviren = grid

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                current = set()

                if i > 0:
                    for x in dp[j]:
                        current.add(x ^ grid[i][j])

                if j > 0:
                    for x in dp[j - 1]:
                        current.add(x ^ grid[i][j])

                dp[j] = current

        return min(dp[-1])