class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        for char in s:
            if char != "*":
                stack.append(char)
            elif stack:
                stack.pop(-1)
        return "".join(stack)