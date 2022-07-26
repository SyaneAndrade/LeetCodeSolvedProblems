class Solution:
    def search(self, nums, target: int) -> int:
        if nums == []:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        pivot = int(len(nums)/2)
        
        if target < nums[pivot]:
            return self.search_binary(0, pivot, nums, target)
        else:
            return self.search_binary(pivot, len(nums), nums, target)
    
    def search_binary(self, begin, final, nums, target):
        i = begin
        while(i < final):
            if nums[i] == target:
                return i
            else:
                i+=1
        return -1
        

if __name__=="__main__":
    sol = Solution()

    nums = [-1,0,3,5,9,12]

    print(sol.search(nums, 9))