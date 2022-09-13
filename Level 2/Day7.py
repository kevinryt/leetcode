import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def height(p):
            if not p: return 0       
                            
            left, right = height(p.left), height(p.right)
            self.ans = max(self.ans, left + right)   
            
            return 1 + max(left, right)
            
        height(root)
        return self.ans

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(node, num):
            if node == None: return 0
            ans = 0
            if node.val == num:
                ans += 1
            ans += dfs(node.left, num - node.val)
            ans += dfs(node.right, num - node.val)
            return ans

        if root == None: return 0

        return dfs(root, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)

    def pathSum_memory(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ans = 0
        cache = collections.defaultdict(int)
        cache[0] = 1

        def dfs(node, sum):
            if not node: 
                return
            
            sum += node.val
            self.ans += cache[sum - target]
            cache[sum] += 1
            dfs(node.left, sum)
            dfs(node.right, sum)
            cache[sum] -= 1 

        dfs(root, 0)
        return self.ans