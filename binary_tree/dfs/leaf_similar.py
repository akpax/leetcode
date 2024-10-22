# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaves1 = []
        self.leaves2 = []
        def find_leaves(node,leaves):
            if node:
                if not node.left and not node.right:
                    leaves.append(node.val)
                    return
                find_leaves(node.left, leaves)
                find_leaves(node.right, leaves)

        find_leaves(root1,self.leaves1)
        find_leaves(root2,self.leaves2)
        return self.leaves1 == self.leaves2
        