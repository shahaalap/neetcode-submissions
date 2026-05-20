class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            count = nums[i]
            result = False
            while count > 0:
                if i + count < n and dp[i + count]:
                    result = True
                    break
                count -= 1
            dp[i] = result

        return dp[0]