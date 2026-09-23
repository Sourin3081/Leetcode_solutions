from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        n = len(intervals)

        # (left, right, weight, original_index)
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort()

        starts = [x[0] for x in arr]

        # next_pos[i] = first interval whose left endpoint > arr[i].right
        next_pos = [0] * n

        for i in range(n):
            r = arr[i][1]
            next_pos[i] = bisect_left(starts, r + 1)

        # dp[i][c] = best result starting from i
        # when we can choose at most c intervals.
        #
        # Each state:
        # (total_weight, tuple_of_sorted_original_indices)

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            # Higher score wins
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same score -> lexicographically smaller list wins
            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):

            l, r, w, original_idx = arr[i]

            for c in range(1, 5):

                # Option 1: skip current interval
                skip = dp[i + 1][c]

                # Option 2: take current interval
                next_weight, next_indices = dp[next_pos[i]][c - 1]

                indices = list(next_indices)
                indices.append(original_idx)
                indices.sort()

                take = (
                    w + next_weight,
                    tuple(indices)
                )

                dp[i][c] = better(skip, take)

        # IMPORTANT:
        # dp[0][4] is (score, indices)
        # Return ONLY indices
        return list(dp[0][4][1])