
from binary_search import Solution

class Solution:
    def search(self, nums, target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums))


    def binary_search(self, nums, target, begin, final):
        sub_vetor = nums[begin:final:]

        if sub_vetor == []:
            return -1

        pivot = int(len(sub_vetor)/2)

        if sub_vetor[pivot] == target:
            return pivot + begin
        
        if sub_vetor[pivot] < target:
            return self.binary_search(nums, target, final - pivot, final)
        else:
            return self.binary_search(nums, target, begin, begin + pivot)


sol = Solution()
nums = [-1,0,3,5,9,12]
# nums = [0,1,2,3,4,5,6,7,8,9,10]
nums
result = sol.search(nums, -1)
print(result)

if __name__=='__main__':
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    result = sol.search(nums, 9)
    print(result)