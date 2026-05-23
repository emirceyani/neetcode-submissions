# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check_nodes(r1, r2):

            if ((r1 is None) and (r2 is not None)) or ((r1 is not None) and (r2 is None)):
                return False
            elif (r1 is None) and (r2 is None):
                return True
            elif r1.val != r2.val:
                return False
            else:
                return True
        
        def inorder(r1, r2):
            if not r1 and not r2:
                return True
            if not check_nodes(r1, r2):
                return False
            if not inorder(r1.left , r2.left):
                return False
            if not inorder(r1.right , r2.right):
                return False
            return True
        return inorder(p,q)