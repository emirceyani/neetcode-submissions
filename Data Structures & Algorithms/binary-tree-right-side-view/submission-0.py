# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        queue = deque()

        if root:
            queue.append(root)
            self.res.append(root.val)
        level = 0
        while len(queue) > 0:
            lvl = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    lvl.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    lvl.append(curr.right.val)
            if len(lvl) >0:
                self.res.append(lvl[-1])
            level += 1
        return self.res