# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a=list1
        b=list2

        if a==None and b==None:
            return None
        elif a!=None and b==None:
            head=a
        elif a==None and b!=None:
            head=b
        else:
            if a.val<b.val:
                head=a
                a=a.next
                c=head
            else:
                head=b
                b=b.next
                c=head
            while a!=None and b!=None:
                if a.val<b.val:
                    c.next=a
                    a=a.next
                    c=c.next
                    
                else:
                    c.next=b
                    b=b.next
                    c=c.next
            if a==None:
                c.next=b
            elif b==None:
                c.next=a
        return head
                
        