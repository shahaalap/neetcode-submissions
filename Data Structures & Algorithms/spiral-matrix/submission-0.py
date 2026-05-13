class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j , k , l = 0, len(matrix) - 1, 0, len(matrix[0]) -1
        result = []

        while i <= j  and k <= l :
            for col in range(k, l + 1):
                result.append(matrix[i][col])
            
            i += 1
            
            for row in range(i,j + 1):
                result.append(matrix[row][l])
            
            l -= 1

            if i > j  or k > l:
                break
                
            for col in range(l , k - 1, -1):
                result.append(matrix[j][col])
            
            j -= 1
            
            for row in range(j , i - 1, - 1):
                result.append(matrix[row][k])
            
            k += 1

        return result


