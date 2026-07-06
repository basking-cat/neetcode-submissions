# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # compare the first nodes in each linked list
        # use curr, next as pointers
        # choose the smaller one as the next node of curr
        # repeat this until both list 1 and 2 are empty
        # create a dummy node first, and return dummy.next at the end
        # compare two lists while both of them is not empty, and just concatinate the rest of a list at the end (to avoid error when executing None.val)

        dummy = ListNode(0) # common approach
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        # !!those two conditions below doesn't happen at the same time!!
        # if not list1:
        #     curr.next = list2
        # if not list2:
        #     curr.next = list1

        return dummy.next