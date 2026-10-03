class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        longest = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # This unmatched ')' becomes the new boundary.
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest