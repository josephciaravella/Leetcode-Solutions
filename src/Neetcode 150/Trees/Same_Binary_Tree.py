class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        if not p and not q:
            return True
        
        def walk(p, q):
            if not p and not q:
                return

            if p and q and p.val == q.val:
                    walk(p.left, q.left)
                    walk(p.right, q.right)
            else:
                self.same = False
        
        walk(p, q)
        return self.same