class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # DFS
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1