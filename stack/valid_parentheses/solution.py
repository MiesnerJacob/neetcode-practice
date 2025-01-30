class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {"}": "{", ")": "(", "]": "["}
        for char in list(s):
            if char in parens.keys():
                if stack == []:
                    stack.append(char)
                elif stack[-1] == parens[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return stack == []