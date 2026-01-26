# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def construct(left, right):
            # Base Case: if there are no elements to process
            if left > right:
                return None

            # 1. Select the root value and increment the pointer
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # 2. Split the inorder list using the map
            mid = mapping[root_val]

            # 3. Recursively build the subtrees
            # IMPORTANT: You MUST build the left before the right 
            # because that's the order they appear in preorder!
            root.left = construct(left, mid - 1)
            root.right = construct(mid + 1, right)

            return root

        return construct(0, len(inorder) - 1)
    

# Gemini did all of this