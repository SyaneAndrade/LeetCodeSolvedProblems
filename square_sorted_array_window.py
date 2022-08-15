


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        for i in range(n-1, -1, -1):
            if(abs(nums[left]) > abs(nums[right])):
                number = nums[left]
                left += 1
            else:
                number = nums[right]
                right -= 1
            result[i] = number * number
        return result