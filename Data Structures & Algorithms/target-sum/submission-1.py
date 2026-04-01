class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0

        def dfs(i, slate):
            nonlocal result
            if i == len(nums):
                if sum(slate) == target:
                    result += 1
                return
            
            # +
            slate.append(nums[i])
            dfs(i + 1, slate)
            slate.pop()

            #-
            slate.append(-nums[i])
            dfs(i + 1, slate)
            slate.pop()

        dfs(0, [])
        return result
