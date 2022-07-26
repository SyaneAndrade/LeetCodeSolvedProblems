"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 1:
            return
        zeros = []
        numes = []
        i = 0
        while(i < size):
            if nums[i] == 0:
                zeros.append(nums[i])
            else:
                numes.append(nums[i])
            i+=1
        nums.clear()
        nums.extend(numes)      
        nums.extend(zeros)



nums = [0,1,0,3,12]

nums = [0, 0]

sol = Solution()

sol.moveZeroes(nums)

print(nums)