class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digithash = {
                '2' : ['a', 'b', 'c'],
                '3' : ['d', 'e', 'f'],
                '4' : ['g', 'h', 'i'],
                '5' : ['j', 'k', 'l'],
                '6' : ['m', 'n', 'o'],
                '7' : ['p', 'q', 'r', 's'],
                '8' : ['t', 'u', 'v'],
                '9' : ['w', 'x', 'y', 'z']
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

            
