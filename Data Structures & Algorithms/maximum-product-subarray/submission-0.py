class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result ,total = nums[0], len(nums)
        prefix = suffix = 1

        for i,n in enumerate(nums):
            prefix *= n
            suffix *= nums[total - 1 - i]

            result = max(result, prefix, suffix)

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return result