# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.right_nodes = []
        self.max_height = -float(inf)
        def dfs(node, height):
            if node:
                if height > self.max_height:
                    self.right_nodes.append(node.val)
                    self.max_height = height
                dfs(node.right, height + 1)
                dfs(node.left, height + 1)
        
        dfs(root, 0)
        return self.right_nodes
