# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def preorder(node):
            if node is None:
                return

            # Visit Root
            result.append(node.val)

            # Visit Left
            preorder(node.left)

            # Visit Right
            preorder(node.right)

        preorder(root)

        return result
