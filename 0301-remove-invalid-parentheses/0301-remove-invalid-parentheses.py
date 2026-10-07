class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(text):
            balance = 0

            for char in text:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False

            return balance == 0

        level = {s}

        while True:
            valid = [text for text in level if is_valid(text)]

            if valid:
                return valid

            next_level = set()

            for text in level:
                for i, char in enumerate(text):
                    if char not in '()':
                        continue

                    # Removing adjacent identical parentheses
                    # produces the same result.
                    if i > 0 and text[i] == text[i - 1]:
                        continue

                    candidate = text[:i] + text[i + 1:]
                    next_level.add(candidate)

            level = next_level