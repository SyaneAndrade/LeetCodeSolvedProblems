"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""


class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                print(cell)
                print(matrix[i][j])
                if cell := matrix[i][j]:
                    bottom = matrix[i+1][j] if i < m - 1 else float('inf')
                    right = matrix[i][j+1] if j < n - 1 else float('inf')
                    matrix[i][j] = min(cell, bottom + 1, right + 1)
        return matrix
    

sol = Solution()

# mat = [[0,0,0],[0,1,0],[1,1,1]]
# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [ [0,1,0,1,1],
        [1,1,0,0,1],
        [0,0,0,1,0],
        [1,0,1,1,1],
        [1,0,0,0,1]]
print(sol.updateMatrix(mat))

