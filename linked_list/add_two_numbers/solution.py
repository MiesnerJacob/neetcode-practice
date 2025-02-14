# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        curr1 = l1
        while curr1:
            nums1.append(curr1.val)
            curr1 = curr1.next

        nums2 = []
        curr2 = l2
        while curr2:
            nums2.append(curr2.val)
            curr2 = curr2.next

        num1 = int("".join([str(i) for i in nums1[::-1]]))
        num2 = int("".join([str(i) for i in nums2[::-1]]))
        num3 = num1 + num2

        result_nums = [int(i) for i in str(num3)][::-1]

        output_nodes = []
        for i in result_nums:
            output_nodes.append(ListNode(val=i))

        last = None
        for i in output_nodes:
            if last != None:
                last.next = i
            last = i
        
        return output_nodes[0]
