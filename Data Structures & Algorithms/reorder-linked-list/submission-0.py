# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # what we have to do is...
        #   - alternate between the first and second halves of this list
        #   - keep doing it
        # combination of 3 basic linked list problems
        # reverse the last half, slow/fast pointers to find the middle, merge two linked lists
        # since we can't go back to the previous element in a linked list, we have to reverse the second half to make it possible

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        sec_curr = slow.next
        slow.next = None # separate the first and second halves of the list

        while sec_curr: # curr stops at None, so the first element of the reversed list is prev
            next_node = sec_curr.next
            sec_curr.next = prev
            prev = sec_curr
            sec_curr = next_node
            
        curr = head
        while prev: # since prev's length is shorter than or equal to the first half
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1

            head = tmp1
            prev = tmp2

        