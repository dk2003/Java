class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        map = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != map[char]:
                    return False
        return True if len(stack) == 0 else False
