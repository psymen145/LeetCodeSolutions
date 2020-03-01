# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = res = ListNode(-1)
        
        carry = False
        
        while l1 is not None or l2 is not None or carry:
            if l1 is None and l2 is not None:
                if carry:
                    tmp_val = l2.val + 1
                else:
                    tmp_val = l2.val
                
                if tmp_val >= 10:
                    carry = True
                    tmp_val -= 10
                else:
                    carry = False
                    
                res.next = ListNode(tmp_val)
                res = res.next
                l2 = l2.next
            elif l2 is None and l1 is not None:
                if carry:
                    tmp_val = l1.val + 1
                else:
                    tmp_val = l1.val
                    
                if tmp_val >= 10:
                    carry = True
                    tmp_val -= 10
                else:
                    carry = False
                    
                res.next = ListNode(tmp_val)
                res = res.next
                l1 = l1.next
            elif l1 is None and l2 is None and carry:
                res.next = ListNode(1)
                res = res.next
                carry = False
            elif l1 is not None and l2 is not None:
                if carry:
                    tmp_val = l1.val + l2.val + 1
                else:
                    tmp_val = l1.val + l2.val
                
                if tmp_val >= 10:
                    carry = True
                    tmp_val -= 10
                else:
                    carry = False
                    
                res.next = ListNode(tmp_val)
                res = res.next
                l2 = l2.next
                l1 = l1.next
                
        return head.next
                
                    
                