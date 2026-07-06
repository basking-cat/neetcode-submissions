# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use recursive approach since we have to check both left and right subtrees
        # return boolean in each step

        def validate(node, min_val, max_val): # to pass down min and max in each path
            if not node:
                return True
            if not (node.val > min_val and node.val < max_val):
                return False
            
            
            # if the current node is valid
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))