class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(open, close, tempresult):
            if open == close == n:
                result.append(''.join(tempresult))
                return

            if open < n:
                tempresult.append('(')
                helper(open + 1, close, tempresult)
                tempresult.pop()

            if close < open:
                tempresult.append(')')
                helper(open, close + 1, tempresult)
                tempresult.pop()

        helper(0, 0, [])

        return result
