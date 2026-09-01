# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def maxDepth(root):

            if root is None:
                return 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            return 1 + max(leftDepth, rightDepth)



        answer = maxDepth(root)

        return(answer)
