class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.broken = False
        if root is None:
            return True
        def walk(root: Optional[TreeNode]):
            if root is None:
                return 0

            left = walk(root.left)
            right = walk(root.right)

            if abs(left - right) > 1:
                self.broken = True

            return 1 + max(left, right)
        
        walk(root)
        return not self.broken