class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        pre[0] = nums[0]
        post[-1] = nums[-1]

        prev = pre[0]
        for i in range(1, len(nums)):
            pre[i] = prev * nums[i]
            prev = pre[i]
            if prev == 0:
                prev = 1
        
        prev = post[-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = prev * nums[i]
            prev = post[i]
            if prev == 0:
                prev = 1


        result = max(max(pre), max(post))
        return result       
