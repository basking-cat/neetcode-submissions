# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers solution (one-pass):
        #   - there are left and right pointers
        #   - move the right pointer forward by n (starting from the first element)
        #   - increment both the left and right pointers until the right one reaches at the end
        #   - l.next = l.next.next
        # time: O(n), space: O(1)

        dummy = ListNode(0, head)
        left, right = dummy, dummy

        for _ in range(n):
            right = right.next

        while right and right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next

        # while right.next and i < n:
        #     right = right.next
        #     i += 1

        # while right and right.next:
        #     right = right.next
        #     left = left.next

        # left.next = left.next.next

        # return head


        # another solution I came up with but didn't use
        #
        # reverse → remove → reverse
        # 1: reverse the entire list
        # 2: move to the (n-1)th element and remove link to nth element
        # 3: reverse the entire list again
        # time: O(n), space: O(1)