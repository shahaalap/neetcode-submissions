class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def helper(i, slate):
            if i == len(nums):
                result.append(slate[:])
                return

            helper(i + 1, slate)

            j = i
            while j < len(nums) and nums[j] == nums[i] :
                j += 1

            for k in range(i, j):
                slate.append(nums[k])
                
            helper(j, slate)
            
            for k in range(i, j):
                slate.pop()

        helper(0, [])
        return result