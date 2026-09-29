class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Answer = C(n + k - 1, 2*k)
        total = n + k - 1
        r = min(2 * k, n - k - 1)

        numerator = 1
        denominator = 1

        for i in range(1, r + 1):
            numerator = numerator * (total - i + 1) % MOD
            denominator = denominator * i % MOD

        return numerator * pow(denominator, MOD - 2, MOD) % MOD