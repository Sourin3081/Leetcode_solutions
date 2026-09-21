class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        result = [0] * k

        # dp[r] = number of subarrays ending at the
        # previous index whose product % k == r
        dp = [0] * k

        for num in nums:
            num %= k

            new_dp = [0] * k

            # Subarray containing only num
            new_dp[num] += 1

            # Extend all previous subarrays with num
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending here to answer
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result