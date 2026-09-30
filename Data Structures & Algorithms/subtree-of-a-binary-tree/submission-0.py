# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        while len(q) > 0:
            head = q.pop(0)
            # dfs and check if subRoot works
            if self.dfs(head, subRoot):
                return True
            # add the 2 children
            if head.left is not None:
                q.append(head.left)
            if head.right is not None:
                q.append(head.right)
        return False

    def dfs(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        if root.val != subRoot.val:
            return False
        return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)
