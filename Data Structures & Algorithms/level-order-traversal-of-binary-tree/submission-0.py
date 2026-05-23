# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def bfs(root):
            queue = deque()

            if root:
                queue.append(root)

            level = 0
            while len(queue) > 0:
                print("level: ", level)
                lvl = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    lvl.append(curr.val)
                    print(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level += 1
                self.res.append(lvl)
        bfs(root)
        return self.res