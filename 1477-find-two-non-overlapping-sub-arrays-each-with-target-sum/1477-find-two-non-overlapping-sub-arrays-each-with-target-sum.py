class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        n = len(arr)
        best = [float('inf')] * n

        left = 0
        total = 0
        min_len = float('inf')
        answer = float('inf')

        for right in range(n):
            total += arr[right]

            # Reduce window if sum becomes greater than target
            while total > target:
                total -= arr[left]
                left += 1

            # Found a subarray with sum = target
            if total == target:
                length = right - left + 1

                # Find another non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])

                # Update minimum length found
                min_len = min(min_len, length)

            best[right] = min_len

        if answer == float('inf'):
            return -1

        return answer