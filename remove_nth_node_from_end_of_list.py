# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = self.findSize(head)
        self.removeNode(head, size-n)
        return head
    
    def findSize(self, head):
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    
    def removeNode(self, head, sub_size):
        node = head
        i = 0
        while(i < (sub_size)):
            node = node.next
            i += 1
        if sub_size == 0:
            node = node.next
        else:
            node.next = node.next.next

if __name__=='__main__':
    # list = [1,2,3,4,5]
    # list = [1,2,3,4,5,6]
    # list = [1]
    node = ListNode(list[0])
    node_aux = node
    for i in range(1, len(list)):
        aux = ListNode(list[i])
        node_aux.next = aux
        node_aux = aux
    
    sol = Solution()

    result = sol.removeNthFromEnd(node, 1)
    print(result)
        