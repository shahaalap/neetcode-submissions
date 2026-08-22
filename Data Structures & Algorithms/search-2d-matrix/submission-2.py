class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0 , len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            x = mid // len(matrix)
            y = mid % len(matrix)

            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                low = mid + 1
            else:
                high = mid - 1

        return False

