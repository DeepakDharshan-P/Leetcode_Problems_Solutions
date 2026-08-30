# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
        # Dummy node
        dummy = ListNode(0)

        # Current pointer
        current = dummy

        # Carry from previous addition
        carry = 0

        while l1 or l2 or carry:

            # Get values
            if l1:
                x = l1.val
            else:
                x = 0

            if l2:
                y = l2.val
            else:
                y = 0

            # Add
            total = x + y + carry

            # Get digit
            digit = total % 10

            # Get carry
            carry = total // 10

            # Create result node
            current.next = ListNode(digit)

            # Move result pointer
            current = current.next

            # Move l1
            if l1:
                l1 = l1.next

            # Move l2
            if l2:
                l2 = l2.next

        return dummy.next
