class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        #Transpose

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #Reverse Columns

        i, j = 0, n - 1

        while i < j:
            for row in range(n):
                matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
                
            i+=1
            j-=1

