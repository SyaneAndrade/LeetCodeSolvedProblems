# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# [1,3,5,6]
# 0


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        return self.searchByPos(nums, target, 0, len(nums))

    def searchByPos(self, nums, target, begin, final):
        sub_vetor = nums[begin : final]
        if len(sub_vetor) == 1:
            if sub_vetor[0] >= target:
                return begin
            else:
                return begin + 1

        pivot = len(sub_vetor) // 2

        if sub_vetor[pivot] == target:
            return pivot + begin
        if sub_vetor[pivot] < target:
            return self.searchByPos(nums, target, final - pivot, final)
        return self.searchByPos(nums, target, begin, begin + pivot)

sol = Solution()

nums = [1,3,5,6]

x = sol.searchInsert(nums, -3)

x