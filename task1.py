from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headset = set()
        curr = headA
        while curr:
            headset.add(curr)
            curr = curr.next
        temp = headB
        while temp:
            if temp in headset:
                return temp
            temp = temp.next
        return None