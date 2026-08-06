# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return None
        r=[]
        curr=head
        
        while curr:
            r.append(curr.val)
            curr=curr.next
        
        r.sort()

        curr=head
        for num in r:
            curr.val = num
            curr=curr.next

        return head
        