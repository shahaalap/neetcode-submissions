class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twosum(nums, total):
            result = []

            i , j = 0, len(nums) - 1

            while i < j:

                if nums[i] + nums[j] == total:
                    result.append([nums[i], nums[j]])
                    i+= 1
                    j-=1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif nums[i] + nums[j] < total:
                    i += 1
                else:
                    j -= 1
                
               

            return result


        result = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            tresult = twosum(nums[i + 1:] , -nums[i])
            if tresult:
                for x in tresult:
                    x.append(nums[i])
                    result.append(x)

        return result