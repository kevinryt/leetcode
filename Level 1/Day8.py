from syslog import LOG_WARNING


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

    def lowestCommonAncestor_recursive(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        def find_ancestor(node, low, high):
            if low <= node.val and high >= node.val:
                return node
            elif high < node.val:
                return find_ancestor(node.left, low, high)
            elif low > node.val:
                return find_ancestor(node.right, low, high)
        
        return find_ancestor(root, low, high)
    
    def lowestCommonAncestor_loop(self, root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


        