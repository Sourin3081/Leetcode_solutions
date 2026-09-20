class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i in range(len(s)):
            reverse_pos = 26 - (ord(s[i]) - ord('a'))
            string_pos = i + 1

            total += reverse_pos * string_pos

        return total