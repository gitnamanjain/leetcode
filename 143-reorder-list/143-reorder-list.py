# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]):
        left = head
        right = self.reverseList(self.getMiddleNode(head))
        self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]):
        while right:
            stash1=left.next
            stash2=right.next
            left.next=right
            right.next=stash1
            left,right=stash1,stash2

    def getMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondhalf = slow.next
        slow.next = None
        return secondhalf

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        minusone = None
        while head:
            stash = head.next
            head.next = minusone
            minusone = head
            head = stash
        return minusone