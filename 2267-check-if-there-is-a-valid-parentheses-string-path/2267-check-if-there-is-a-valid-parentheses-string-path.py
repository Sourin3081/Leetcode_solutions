class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] != '(' or grid[m - 1][n - 1] != ')':
            return False

        # dp[j] stores possible unmatched '(' counts.
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    previous = {0}
                else:
                    previous = set(dp[j])  # From above
                    if j > 0:
                        previous.update(dp[j - 1])  # From left

                change = 1 if grid[i][j] == '(' else -1
                remaining = (m - 1 - i) + (n - 1 - j)

                dp[j] = set()
                for balance in previous:
                    new_balance = balance + change

                    if 0 <= new_balance <= remaining:
                        dp[j].add(new_balance)

        return 0 in dp[n - 1]