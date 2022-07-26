class Solution:
    def twoSum(self, nums, target: int):
        hash_nums = {}

        for i in range(0, len(nums)):
            hash_nums[nums[i]] = i
        
        for key in hash_nums:
            if target < 0 and key < 0:
                target_2 = target + abs(key)
            else:
                target_2 = target - key
            if hash_nums[target_2]:
                return [hash_nums[key] + 1,hash_nums[target_2] + 1]
        


if __name__=="__main__":
    sol = Solution()
    nums = [0, 0]



    print(sol.twoSum(nums, 1))