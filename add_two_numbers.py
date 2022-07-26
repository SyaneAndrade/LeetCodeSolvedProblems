
import functools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            keep_going = True
            l1_values = []
            l2_values = []
            while keep_going:
                if l1: 
                    l1_values.append(l1.val)
                    l1 = l1.next
                if l2:
                    l2_values.append(l2.val)
                    l2 = l2.next
                
                if not (l1 or l2):
                    keep_going = False
                    
            l1_order = l1_values[::-1]
            l2_order = l2_values[::-1]

            # l1_number = functools.reduce(lambda total, d: 10 * total + d, l1_order, 0)
            # l2_number = functools.reduce(lambda total, d: 10 * total + d, l2_order, 0)

            l1_number = "".join(map(str, l1_order))
            l2_number = "".join(map(str, l2_order))

            sum = int(l1_number) + int(l2_number)


            list_sum = list(map(int, str(sum)))

            result = list_sum[::-1]
            
            return self.criaNodeList(result)
            
        def criaNodeList(self, result_list):
            
            node = ListNode(result_list[0])
            node_aux = node
            for i in range(1, len(result_list)):
                aux = ListNode(result_list[i])
                node_aux.next = aux
                node_aux = aux
            return node

if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

#     [2,4,3]
#     [5,6,4]
# [0]
# [0]
# [9,9,9,9,9,9,9]
# [9,9,9,9]
    
    sol = Solution()

    l1_node = sol.criaNodeList(l1)
    l2_node = sol.criaNodeList(l2)

    print(sol.addTwoNumbers(l1_node, l2_node))


