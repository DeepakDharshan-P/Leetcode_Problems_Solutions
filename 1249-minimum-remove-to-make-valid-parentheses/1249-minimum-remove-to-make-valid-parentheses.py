class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        remove = set()

        # First pass
        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':

                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        # Any '(' remaining in stack is invalid
        while stack:
            remove.add(stack.pop())

        # Build answer
        result = []

        for i in range(len(s)):
            if i not in remove:
                result.append(s[i])

        return ''.join(result)