class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n ,m, o = len(s1), len(s2), len(s3)

        if n +m != o:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and dp[i + 1][j] and s1[i] == s3[i + j]:
                    dp[i][j] = True
                
                if j < m and dp[i][j + 1] and s2[j] == s3[i + j]:
                    dp[i][j] = True

        return dp[0][0]