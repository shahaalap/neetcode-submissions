class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            cur = abs(n)
            if nums[cur - 1] < 0:
                return cur

            nums[cur - 1] *= -1
