class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digithash = {
                '2' : 'abc',
                '3' : 'def',
                '4' : 'ghi',
                '5' : 'jkl',
                '6' : 'mno',
                '7' : 'pqrs',
                '8' : 'tuv',
                '9' : 'wxyz'
            }
        result = []
        if not digits:
            return result

        def dfs(i, slate):
            if i == len(digits):
                result.append(''.join(slate))
                return

            for c in digithash[digits[i]]:
                slate.append(c)
                dfs(i + 1, slate)
                slate.pop()

        
        dfs(0, [])
        return result

            
