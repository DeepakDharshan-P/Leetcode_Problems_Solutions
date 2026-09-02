class Solution:
    def lowestCommonAncestor(self, root, p, q):

        # If tree is empty
        if root is None:
            return None

        # If we found p or q
        if root == p or root == q:
            return root

        # Search left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q are found on different sides
        if left and right:
            return root

        # If found on left side
        if left:
            return left

        # If found on right side
        return right