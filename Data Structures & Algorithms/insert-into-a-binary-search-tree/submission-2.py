# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        prev = None

        while cur:
            prev = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        if val > prev.val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)


        return root