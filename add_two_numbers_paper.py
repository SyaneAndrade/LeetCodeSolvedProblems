
#     [2,4,3]
#     [5,6,4]
#     342
#    +465
#    –––––
#     807
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            solution = ListNode()
            aux = solution
            up = 0
            while l1 or l2 or up:
                val_1 = l1.val if l1 else 0
                val_2 = l2.val if l2 else 0
                
                sum = val_1 + val_2 + up

                result_node = sum % 10

                up = sum // 10

                aux.next = ListNode(result_node)
                aux = aux.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            return solution

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

    
    sol = Solution()

    l1_node = sol.criaNodeList(l1)
    l2_node = sol.criaNodeList(l2)

    result = sol.addTwoNumbers(l1_node, l2_node)

    while result:
        print(result.val)
        result = result.next

