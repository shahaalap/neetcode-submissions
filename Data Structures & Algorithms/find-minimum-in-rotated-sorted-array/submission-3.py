class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        result = 1001

        while i < j:
            mid = i + (j - i) // 2
            result = min(result, nums[mid])

            if nums[j] < nums[mid]:
                i = mid + 1
            else:
                j = mid

        return nums[i]