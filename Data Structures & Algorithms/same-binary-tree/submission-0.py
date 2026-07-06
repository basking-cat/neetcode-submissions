# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # - structurally identical
        # - nodes have the same value
        # if both p and q exist and have the same value, check child nodes recursively

        if not p and not q: # base case
            return True
        if not p or not q or p.val != q.val: # if only one of p and q is None, or the values are different
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

