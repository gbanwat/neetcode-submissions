# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d={}
        dummy=head
        while dummy!=None:
            if dummy in d:
                return True
            else:
                d[dummy]="visited"
                dummy=dummy.next
        return False
        