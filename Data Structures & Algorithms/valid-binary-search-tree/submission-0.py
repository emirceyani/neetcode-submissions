# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lval, rval):
            if not node:
                return True
            if not (lval < node.val < rval):
                return False
            return valid(node.left,lval, node.val) and valid(node.right, node.val, rval)
        return valid(root, float("-inf"), float("inf"))
        