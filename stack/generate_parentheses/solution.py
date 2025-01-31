class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(open_parens_count, closed_parens_count):
            if open_parens_count == closed_parens_count == n:
                res.append("".join(stack))
                return

            if open_parens_count < n:
                stack.append("(")
                backtracking(open_parens_count + 1, closed_parens_count)
                stack.pop()

            if closed_parens_count < open_parens_count:
                stack.append(")")
                backtracking(open_parens_count, closed_parens_count + 1)
                stack.pop()

        backtracking(0,0)
        return res

