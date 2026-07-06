# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # basic bfs problem
        # time: O(n), space: O(n) (there are possibly n/2 nodes in the queue at its maximum)
        if not root:
            return []
    
        res = []
        queue = deque([root])
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left) # add to queue only if the left/right node exists
                if node.right: queue.append(node.right)
            res.append(level)
        
        return res

