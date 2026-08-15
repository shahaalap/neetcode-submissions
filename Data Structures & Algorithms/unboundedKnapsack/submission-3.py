class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[None for _ in range(capacity + 1)] for _ in range(len(profit) + 1)]

        def helper(i, remainingCapacity):

            if memo[i][remainingCapacity]:
                return memo[i][remainingCapacity]

            if i == len(profit):
                return 0

            result = 0

            #Exclude
            result = helper(i + 1, remainingCapacity)

            #Include
            if remainingCapacity - weight[i] >= 0:
                result = max(result, profit[i] + helper(i, remainingCapacity - weight[i]))
            
            memo[i][remainingCapacity] = result
            return result

        return helper(0, capacity)