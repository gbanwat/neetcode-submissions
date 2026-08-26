# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        a=head
        while a!=None:
            length+=1
            a=a.next

#If DELETING THE FIRST ELEMENT OF THE LL
        if length==n:
            return head.next

        remove=length-n
        c=0
        b=head
        while c<remove-1:
            b=b.next
            c+=1
#IF THE ELEMENT TO BE DELETED IS THE LAST ELEMENT IN THE LIST
        if b.next.next!=None:
            nn=b.next.next
            b.next=nn
        elif b.next.next==None:
            b.next=None
        return head
        




        