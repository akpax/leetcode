# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float(inf)
        level, ans = 0,0
        queue = [root]
        while queue:
            level += 1
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                    max_sum = level_sum
                    ans = level
        return ans