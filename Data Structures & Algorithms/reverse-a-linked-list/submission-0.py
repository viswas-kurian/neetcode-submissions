# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        dummy = ListNode(0)
        d = dummy

        while temp:
            stack.append(temp.val)
            temp = temp.next

        while stack:
            d.next = ListNode(stack.pop())
            d = d.next

        return dummy.next