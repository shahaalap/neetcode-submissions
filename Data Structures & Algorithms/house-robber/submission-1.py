class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            include = dfs(i + 2) + nums[i]
            exclude = dfs(i + 1)
            result = max(include, exclude)
            cache[i] = result
            return result


        return dfs(0)