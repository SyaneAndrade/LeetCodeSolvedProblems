"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

"""

class Solution:
    def sortedSquares(self, nums):
        squares = []
        negative_squares = []
        i = 0
        j = 0
        before = 0
        while(i < len(nums)):
            if nums[i] < 0:
                negative_squares.append(pow(nums[i], 2))
                negative_squares_aux = negative_squares[::-1]
            else:
                num_square = pow(nums[i], 2)
                num_square
                before
                j
                while(j < len(negative_squares_aux)):
                    if (negative_squares_aux[j] <= num_square) and (negative_squares_aux[j] >= before):
                        before = negative_squares_aux[j]
                        squares.append(negative_squares_aux[j])
                        j += 1
                    else:
                        break
                before = num_square
                squares.append(num_square)
            i += 1
        if len(squares) == 0:
            return negative_squares_aux
        elif j < len(negative_squares_aux):
            squares.extend(negative_squares_aux[j:])
        return squares

sol = Solution()
nums = [-2, 0]
result = sol.sortedSquares(nums)
print(result)