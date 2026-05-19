class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        
        def helper(i, previnx):
            
            if i == len(nums):
                return 0

            if (i, previnx) in dp:
                return dp[(i, previnx)]

            result = 0

            #include
            if previnx == -1 or nums[i] > nums[previnx]:
                result = 1 + helper(i + 1, i)
            
            #exclude
            result = max(result, helper(i + 1, previnx))
            dp[(i, previnx)] = result
            return result


        
        return helper(0, -1)

