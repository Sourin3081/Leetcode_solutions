class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        for num in range(1, n + 1):
            x = num
            changed = False
            valid = True

            while x > 0:
                digit = x % 10

                # Invalid digits
                if digit in (3, 4, 7):
                    valid = False
                    break

                # Digits that change after rotation
                if digit in (2, 5, 6, 9):
                    changed = True

                x //= 10

            if valid and changed:
                count += 1

        return count