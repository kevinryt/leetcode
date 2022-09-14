from collections import deque
import queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return p == q
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root_1, root_2):
            if root_1 and root_2:
                return root_1.val == root_2.val and check(root_1.left, root_2.right) and check(root_1.right, root_2.left)
        
            return root_1 == root_2
    
        return check(root, root)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        dq = deque([root])

        while dq:
            right_node = None
            length = len(dq)

            for i in range(length):
                node = dq.popleft()
                if node:
                    right_node = node
                    dq.append(node.left)
                    dq.append(node.right)
                
            if right_node:
                res.append(right_node.val)

        return res
            