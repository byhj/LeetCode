# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = queue.Queue()
        q.put(root)
        ans = []
        while not q.empty():
            size = q.qsize()
            n = size
            layer = 0
            while size > 0:
                node = q.get()
                layer += node.val
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
                size -= 1
            ans.append(layer/n)
        return ans
                