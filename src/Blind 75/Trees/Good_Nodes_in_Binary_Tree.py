class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        res = 0

        stack = []

        stack.append((root, root.val))

        while len(stack) != 0:
            node, curr_max = stack.pop()
            if node and node.val >= curr_max:
                new_max = node.val
                res += 1
            else:
                new_max = curr_max

            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        
        return res