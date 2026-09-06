class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, tempresult):
            if i == len(nums):
                result.append(tempresult[:])
                return

            #Exclude
            helper(i + 1, tempresult)

            #Include
            tempresult.append(nums[i])
            helper(i + 1, tempresult)
            tempresult.pop()

        helper(0, [])
        return result