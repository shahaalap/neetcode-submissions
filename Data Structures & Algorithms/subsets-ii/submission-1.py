class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []


        def helper(i, tempresult):
            if i == len(nums):
                result.append(tempresult[:])
                return

            #count duplicates
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            duplen = j - i

            #Exclude
            helper(j, tempresult)
            
            #Include
            for _ in range(duplen):
                tempresult.append(nums[i])
                helper(j , tempresult)
            
            
            for _ in range(duplen):
                tempresult.pop()

        
        helper(0 , [])
        return result