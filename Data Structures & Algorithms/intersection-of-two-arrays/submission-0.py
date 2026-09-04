class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []

        def binary_search(target):
            i , j = 0, len(nums2) - 1

            while i < j:
                mid = (i + j) // 2

                if target == nums2[mid]:
                    return True
                elif target > nums2[mid]:
                    i = mid + 1
                else:
                    j = mid - 1

            return nums2[i] == target

        for i, n1 in enumerate(nums1):
            if i > 0 and nums1[i] == nums1[i - 1]:
                continue

            if binary_search(n1):
                result.append(n1)

        return result