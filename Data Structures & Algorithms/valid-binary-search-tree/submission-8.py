# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True

        if root.left:
            return self.isValidBST(root.left) and root.left.val < root.val

        if root.right:
            return self.isValidBST(root.right) and root.right.val > root.val

