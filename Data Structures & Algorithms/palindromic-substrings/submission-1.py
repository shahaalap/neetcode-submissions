class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def palindromecount(i, j):
            result = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i-=1
                j+=1

            return result

        result = 0
        for i in range(len(s)):
            result += palindromecount(i, i)
            result += palindromecount(i, i + 1)

        return result
