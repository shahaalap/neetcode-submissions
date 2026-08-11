class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        x = len(obstacleGrid)
        y = len(obstacleGrid[0])

        memo = [[None for _ in range(y + 1)] for _ in range(x + 1)]

        def helper(i, j):
            if memo[i][j] is not None:
                return memo[i][j]

            if i == x or j == y or obstacleGrid[i][j] == 1:
                memo[i][j] = 0
                return 0

            if i == x - 1 and j == y - 1:
                memo[i][j] = 1
                return 1

            memo[i][j] = helper(i + 1, j) + helper(i, j + 1)
            return memo[i][j]


        helper(0, 0)
        return memo[0][0]