class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            cur = abs(n)
            curval = nums[cur - 1]
            if curval < 0:
                return cur
            nums[cur - 1] *= -1