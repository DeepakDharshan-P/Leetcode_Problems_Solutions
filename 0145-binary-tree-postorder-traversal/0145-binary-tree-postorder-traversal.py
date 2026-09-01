# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

            result = []

            def postorder(node):
                if node is None:
                    return

                # 1. Visit Left
                postorder(node.left)

                # 2. Visit Right
                postorder(node.right)

                # 3. Visit Root
                result.append(node.val)

            postorder(root)
            return result
