class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(o, c, slate):
            if o == 0 and c == 0:
                result.append(''.join(slate))
                return

            if o > 0:
                slate.append('(')
                helper(o - 1, c + 1, slate)
                slate.pop()

            if c > 0:
                slate.append(')')
                helper(o, c - 1, slate)
                slate.pop()

        helper(n, 0, [])
        return result