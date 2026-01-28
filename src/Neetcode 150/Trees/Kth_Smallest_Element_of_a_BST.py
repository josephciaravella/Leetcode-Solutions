# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.count = 0
        # can go all the way until a leaf, increase count, then set left pointer to null, visit right, then set right pointer to null
        def walk(node):
            if not node:
                return

            # smallest values
            if node.left:
                walk(node.left)
            
            # all smaller values have been counted
            self.count += 1

            # check that we align with k
            if self.count == k:
                self.ans = node.val
           
            # move to the next smallest values
            if node.right:
                walk(node.right) 
        
        walk(root)
        return self.ans