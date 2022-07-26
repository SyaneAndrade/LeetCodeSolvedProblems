# -*- coding: utf-8 -*-
import math

class Solution:
    def maxSubArray(self, nums):
        # eu so posso somar o elemento com que esta do seu lado
        # 0 -> [-2, -1, -4, -5, -3, -2, -7, -3]
        # 1 -> [1, -2, 2, 1, 3, 4, -1, 3]
        # 2 -> [-3, 1, 0, 2, 3, -2, 2]
        # 3 -> [4, 3, 5, 6, 1, 5]
        # 5 -> [-1, 1, 2, -3, 1]
        # 6 -> [2, 3, -2, 2]
        # 7 -> [1, -4, 0]
        # 8 -> [-5, 1]
        # 9 -> [4]
        # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        
        max_sums = []
        size = len(nums)
        max_subarray = -math.inf
        for i in range(0, len(nums)):
            sum_subarray =  0
            for j in range(i, len(nums)):
              sum_subarray += nums[j]
              max_subarray = max(max_subarray, sum_subarray)
        return max_subarray

if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max = sol.maxSubArray(nums)
    print(max)