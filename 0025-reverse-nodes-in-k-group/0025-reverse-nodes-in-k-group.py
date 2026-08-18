# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        check = head

        # Check whether k nodes exist
        for _ in range(k):
            if check is None:
                return head
            check = check.next

        previous = None
        current = head

        # Reverse exactly k nodes
        for _ in range(k):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # Connect this group to the processed remaining list
        head.next = self.reverseKGroup(current, k)

        # Return the new beginning
        return previous