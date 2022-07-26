class Solution:
    def sortArray(self, nums):

        if len(nums) == 1:
            return nums

        divide = int(len(nums)/2)
        
        listA = self.sortArray(nums[0:divide])
        listB = self.sortArray(nums[divide:])
        print(f'A :{listA}')
        print(f'B: {listB}')
        return self.merge(listA, listB)
    
    def merge(self, listA, listB):
        arr_sort = []
        i = j = 0
        while ((i < len(listA)) and (j < len(listB))):
            if listA[i] < listB[j]:
                arr_sort.append(listA[i])
                i += 1
            else:
                arr_sort.append(listB[j])
                j += 1
        arr_sort.extend(listA[i:])
        arr_sort.extend(listB[j:])
        return arr_sort


if __name__ == '__main__':
    sol = Solution()
    sort = sol.sortArray([3,4,6,7,2,1])
    print(sort)