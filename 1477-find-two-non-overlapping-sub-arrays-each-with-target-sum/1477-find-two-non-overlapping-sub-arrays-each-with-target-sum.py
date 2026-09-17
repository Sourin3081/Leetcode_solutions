class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [INF] * n

        left = 0
        total = 0
        min_len = INF
        answer = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                # Check for a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        if answer == INF:
            return -1

        return answer