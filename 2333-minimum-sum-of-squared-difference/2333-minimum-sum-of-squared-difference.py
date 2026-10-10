
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            # Operations needed to make every difference <= mid
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        used = sum(max(0, d - level) for d in diffs)
        remaining = k - used

        # Reduce differences above level to level
        ans = sum(min(d, level) ** 2 for d in diffs)

        # Use remaining operations to reduce some level values by 1
        ans -= remaining * (2 * level - 1)

        return ans
