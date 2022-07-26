from email.mime import base
from hashlib import new
from mailbox import NoSuchMailboxError
from tkinter import W


class Solution:
    def sortArray(self, nums):
        base_group = 1

        while(True):
            i = 0
            end_i = j = i + base_group
            end_j = j + base_group
            new_list = []

            while i < len(nums):
                self.merge(nums, new_list, i, end_i, j, end_j)
                i = end_j
                end_i = j = i + base_group
                end_j = j + base_group
                print(new_list)
            nums = new_list
            base_group *= 2
            if base_group > len(nums):
                break
        return nums

                
    def merge(self, nums, new_list, i, end_i, j, end_j):
        while i < end_i and j < end_j and j < len(nums):
            if nums[i] <  nums[j]:
                new_list.append(nums[i])
                i += 1
            else:
                new_list.append(nums[j])
                j += 1
        
        while i < end_i and i < len(nums):
            new_list.append(nums[i])
            i += 1
        while j < end_j and j < len(nums):
            new_list.append(nums[j])
            j += 1

if __name__ == '__main__':
    sol = Solution()
    sort = sol.sortArray([3,4,6,7,2,1])
    print(sort)


