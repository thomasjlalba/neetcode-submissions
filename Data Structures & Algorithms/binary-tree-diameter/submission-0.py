# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length, ans = self.dfs(root, 0)
        return ans
        
    def dfs(self, head, maxDiameter):
        if head is None:
            return 0, 0
        
        left, maxLeft = self.dfs(head.left, maxDiameter)
        right, maxRight = self.dfs(head.right, maxDiameter)
        diameter = left + right
        return 1 + max(left, right), max(diameter, maxLeft, maxRight)