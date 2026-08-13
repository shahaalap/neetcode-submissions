class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[None for _ in range(capacity + 1)] for _ in range(len(profit) + 1)]

        def helper(i, capacity):
            if i == len(weight):
                return 0

            if memo[i][capacity]:
                return memo[i][capacity]
            exclude = helper(i + 1, capacity)

            include = 0
            if capacity - weight[i] >= 0:
                include = profit[i] + helper(i + 1, capacity - weight[i])

            result = max(include, exclude)
            memo[i][capacity] = result
            return result

        return helper(0, capacity)
            


