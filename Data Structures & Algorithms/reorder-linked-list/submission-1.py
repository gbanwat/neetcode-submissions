# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f=head
        s=head
        while f.next!=None:
            if f.next.next!=None:
                s=s.next
                f=f.next.next
            else:
                f=f.next
        c=s.next
        s.next=None
        p=None

        while c!=None:
            n=c.next
            c.next=p
            p=c
            c=n
        s1=head
        f1=p
        while s1!=None and f1!=None:
            sn=s1.next
            fn=f1.next
            s1.next=f1
            f1.next=sn
            s1=sn
            f1=fn

        
        
            
        


        
        
        
        