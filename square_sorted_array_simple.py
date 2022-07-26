class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

sol = Solution()
nums = [-2, 0]
result = sol.sortedSquares(nums)
print(result)