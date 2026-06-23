class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def helper(i, total):

            if total > amount:
                return 0

            if total == amount:
                return 1
            
            if i == len(coins):
                return 0
            

            if (i, total) in dp:
                return dp[(i, total)]

            result = helper(i + 1, total) + helper(i , total + coins[i])
            dp[(i,total)] = result
            return result

        return helper(0, 0)
