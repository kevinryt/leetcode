from collections import deque
from turtle import left


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root:
            result.append(root.val)
            for child in root.children:
                result.extend(self.preorder(child, result))
        return result
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque([root])
        res = []
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
        
