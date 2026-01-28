class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # both none types
        if not root and not subRoot:
            return True
        # only root is none
        if not root:
            return False
        
        # validate subtrees
        def isSame(p, q):
            # reached leaf nodes
            if not p and not q:
                return True
            # one is not null and the other is or values are not equal
            if not p or not q or p.val != q.val:
                return False
            # node vals are equal, need to check the left and right trees
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        # start with the original root and subroot
        if isSame(root, subRoot):
            return True
        else:
            # check root's children
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)