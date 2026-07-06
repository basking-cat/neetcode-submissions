# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order solution
        # 1. stack left nodes first until it's None
        # 2. pop stack & go to the right node
        # 3. repeat
        # time: O(2n)=O(n) since each node will be processed exactly twice
        # space: O(h) if the tree is balanced (h=logn), O(n) if the tree is skewed

        node = root
        stack = []

        # while node: think of a tree with all nodes skewed to the right (there'll be a moment when the stack is empty, but there still are nodes unprocessed)
        # while stack: when we've reached the left end or when node.right is None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1 # visit
            if k == 0:
                return node.val
            node = node.right
