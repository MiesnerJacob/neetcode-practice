from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        left_pointer = 0
        right_pointer = len(nodes) - 1
        while left_pointer < right_pointer:
            nodes[left_pointer].next = nodes[right_pointer]
            left_pointer += 1
            if left_pointer >= right_pointer:
                break
            nodes[right_pointer].next = nodes[left_pointer]
            right_pointer -= 1
        
        nodes[left_pointer].next = None
