class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the actual beginning
        n = len(nums) - 1
        i , j = 0, n

        while i < j:
            mid = i + (j - i)//2
          
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid

        minindex = i
        #find target considering new min index

        i , j = 0, n

        if target >= nums[minindex] and target <= nums[j]:
            i = minindex
        else:
            j = minindex - 1

        while i <= j:
            mid = i + (j - i)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return -1
        
