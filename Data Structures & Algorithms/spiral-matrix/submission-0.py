class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j , k , l = 0, len(matrix[0]) - 1 , 0, len(matrix) - 1
        result = []
        while i <= j and k <= l:
            for col in range(i, j + 1):
                result.append(matrix[k][col])
            k += 1
            
            if k > l: break
            for row in range(k, l + 1):
                result.append(matrix[row][j])
            j -= 1

            if i > j: break
            for col in range(j, i - 1, -1):
                result.append(matrix[l][col])
            l -= 1

            if k > l: break
            for row in range(l, k - 1, -1):
                result.append(matrix[row][i])
            i += 1

        return result
