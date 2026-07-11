class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for k in range(len(s)):
            i = j = k

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            if j - i - 1 > len(result):
                result = s[i + 1: j]

            i , j = k, k + 1

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            if j - i - 1 > len(result):
                result = s[i + 1: j]


        return result