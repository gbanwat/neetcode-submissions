# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        h1=a
        carry=0

        while l1!=None and l2!=None:
            t=carry+l1.val+l2.val
            unit=t%10
            carry=t//10
            a.val=unit
            l1=l1.next
            l2=l2.next
            if l1!=None and l2!=None:
                b=ListNode()
                a.next=b
                a=a.next

        if l1==None and l2!=None:
            while l2!=None:
                t=carry+l2.val
                unit=t%10
                carry=t//10

                b=ListNode()
                a.next=b
                a=a.next
                a.val=unit

                l2=l2.next



        elif l1!=None and l2==None:
            while l1!=None:
                t=carry+l1.val
                unit=t%10
                carry=t//10

                b=ListNode()
                a.next=b
                a=a.next
                a.val=unit

                l1=l1.next

        if carry!=0:
            b=ListNode()
            a.next=b
            a=a.next
            a.val=carry
            return h1
        else:
            return h1

            


        