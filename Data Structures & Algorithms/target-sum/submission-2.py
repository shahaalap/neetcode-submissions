class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0

        def dfs(i, cur):
            nonlocal result
            if i == len(nums):
                if cur == target:
                    result += 1
                return
            
            # +
            cur += nums[i]
            dfs(i + 1, cur)
            cur -= nums[i]

            #-
            cur -= nums[i]
            dfs(i + 1, cur)
            cur += nums[i]

        dfs(0, 0)
        return result
