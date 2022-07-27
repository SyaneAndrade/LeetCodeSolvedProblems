# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        size = self.findSize(head)
        return self.findMiddleNode(head, size)
    
    def findSize(self, head):
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    
    def findMiddleNode(self, head, size):
        node = head
        i = 0
        while(i < (size//2)):
            node = node.next
            i += 1
        return node


if __name__=='__main__':
    list = [1,2,3,4,5]
    # list = [1,2,3,4,5,6]
    node = ListNode(list[0])
    node_aux = node
    for i in range(1, len(list)):
        aux = ListNode(list[i])
        node_aux.next = aux
        node_aux = aux
    
    sol = Solution()

    result = sol.middleNode(node)
    print(result)
        
