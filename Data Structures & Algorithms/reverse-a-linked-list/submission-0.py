# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # method 1: iteration
      #  - change links in place
      # method 2: recursion
      #  - go to the end and go backward (space complexity is O(n))
      #
      # we'll use iteration
      # we keep track of three pointers: curr, prev, next
      # when curr is null, the linked list is reversed
      # in each step, change the next val to prev

      curr = head
      prev = None
      while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

      return prev # not curr since curr stops at None