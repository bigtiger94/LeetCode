# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_str = ''
        l2_str = ''
        
        # convert type integer to string
        while(l1.next != None):
            l1_str = str(l1.val) + l1_str
            l1 = l1.next
        l1_str = str(l1.val) + l1_str
        
        while(l2.next != None):
            l2_str = str(l2.val) + l2_str
            l2 = l2.next    
        l2_str = str(l2.val) + l2_str
        
        # sum
        listsum = int(l1_str) + int(l2_str)
        
        # reverse order
        templist = str(listsum)[::-1]
        
        
        firstnode = ListNode()
        list_out = firstnode
        for ii in templist:
            list_out.next = ListNode(val=ii)
            list_out = list_out.next
        return(firstnode.next)
