class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        maxDist = 0

        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    maxDist = max(maxDist, j - i)

        return maxDist