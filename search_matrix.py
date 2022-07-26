class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target

        if matrix == []:
            return False

        pivot_i = int((len(matrix) / 2) - 1)
        ptivot_j = int((len(matrix[0]) / 2) - 1)

        pivot = matrix[pivot_i][ptivot_j]

        if pivot == target:
            return True
        
        if pivot < target:
            return (self.searchMatrix(matrix[:pivot_i][:ptivot_j], target) or
            self.searchMatrix(matrix[:pivot_i][ptivot_j:], target) or
            self.searchMatrix(matrix[pivot_i:][:ptivot_j], target))
        else:
            return (self.searchMatrix(matrix[:pivot_i][ptivot_j:], target) or
                    self.searchMatrix(matrix[pivot_i:][:ptivot_j], target) or
                    self.searchMatrix(matrix[pivot_i:][ptivot_j:], target))
    
        

if __name__=='__main__':
    sol = Solution()
    matrix = [[1,2], [3,4]]

    matrix2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

    print(matrix[:1][:1])
    print(matrix[1:][:1])
    print(matrix[-1][-1])

    isTrue = sol.searchMatrix(matrix2, 20)
    print(isTrue)


    