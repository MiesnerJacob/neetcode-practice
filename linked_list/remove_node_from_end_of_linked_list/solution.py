from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        current = head
        while current:
            nodes.append(current)
            current = current.next

        nodes.pop(-n)

        last = None
        for i in nodes:
            if last:
                last.next = i
            i.next = None
            last = i

        return nodes[0] if nodes else None