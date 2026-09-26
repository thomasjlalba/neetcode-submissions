# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans, maxHeight = self.dfs(root)
        return ans
    
    def dfs(self, head):
        if head is None:
            return True, 0
        
        ans, left = self.dfs(head.left)
        if ans == False:
            return False, 0
        ans, right = self.dfs(head.right)
        if ans == False or abs(left - right) > 1:
            return False, 0
        return True, 1 + max(left, right)
