class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[None for _ in range(len(text2))] for _ in range(len(text1) )]

        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if memo[i][j]:
                return memo[i][j]

            result = 0

            if text1[i] == text2[j]:
                result = 1 + helper(i + 1, j + 1)
            else:
                result = max(helper(i, j + 1), helper(i + 1, j))

            memo[i][j] = result
            return result

        return helper(0, 0)