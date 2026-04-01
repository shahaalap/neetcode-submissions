class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]

            total = 0

            if i == len(nums):
                if cur == target:
                    total += 1
                return total
            
            # +
            cur += nums[i]
            total += dfs(i + 1, cur)
            cur -= nums[i]

            #-
            cur -= nums[i]
            total += dfs(i + 1, cur)
            cur += nums[i]

            cache[(i, cur)] = total
            return total

        return dfs(0, 0)
