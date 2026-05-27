class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispalindrome(s):
            
            i , j = 0 , len(s) - 1

            while i <= j and s[i] == s[j]:
                i += 1
                j -= 1

            return i > j

        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if ispalindrome(s[i:j + 1]):
                    result += 1

        return result