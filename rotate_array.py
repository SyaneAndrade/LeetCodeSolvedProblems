# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


class Solution:
    def rotate(self, nums, k: int):
        size = len(nums)
        while(k > size):
            k = k - len(nums)
        nums_begin = nums[-k:]
        nums_final = nums[:-k]
        nums.clear()
        nums.extend(nums_begin)
        nums.extend(nums_final)

sol = Solution()

# nums = [1,2,3,4,5,6,7]
nums = [1,2]
k = 5
# print(nums[-3])

sol.rotate(nums, k)

print(nums)