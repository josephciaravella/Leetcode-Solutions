class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.valid = True
        def walk_and_valid(node, low, high):
            if not low < node.val < high:
                self.valid = False
                return
            
            if node.left:
                walk_and_valid(node.left, low, node.val)
            if node.right:
                walk_and_valid(node.right, node.val, high)
        
        walk_and_valid(root, float('-inf'), float('inf'))
        return self.valid