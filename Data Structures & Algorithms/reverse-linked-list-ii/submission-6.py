# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head==None or head.next==None or left==right:
            return head
        
        left_prev=ListNode()
        left_node=head

        for i in range(left-1):
            left_prev=left_node
            left_node=left_node.next

        prev=None
        curr=left_node

        for j in range(left,right+1):
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        
        left_node.next=curr

        if left!=1:
            left_prev.next=prev
            return head
        else:
            return prev
            
        

        

        





        








        




        