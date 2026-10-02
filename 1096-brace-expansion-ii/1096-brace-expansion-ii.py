class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        n = len(expression)

        def parse(i):
            result = set()
            current = {""}

            while i < n and expression[i] != "}":
                char = expression[i]

                if char == ",":
                    result.update(current)
                    current = {""}
                    i += 1
                    continue

                if char == "{":
                    words, i = parse(i + 1)
                else:
                    words = {char}
                    i += 1

                current = {
                    prefix + word
                    for prefix in current
                    for word in words
                }

            result.update(current)

            # Skip the closing brace, if present.
            if i < n and expression[i] == "}":
                i += 1

            return result, i

        words, _ = parse(0)
        return sorted(words)