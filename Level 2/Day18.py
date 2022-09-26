import collections

class Solution:
    def findCircleNum(self, isConnected):
        if not isConnected: return 0
        row = len(isConnected)
        seen = set()
        
        def dfs(city_1):
            for city_2, connection in enumerate(isConnected[city_1]):
                if (connection == 1) and (city_2 not in seen):
                    seen.add(city_2)
                    dfs(city_2)
        
        prov = 0
        for i in range(row):
            if i not in seen: 
                dfs(i)
                prov += 1
        
        return prov

    def combinationSum_DP(self, candidates, target):

        candidates.sort()
        memo = collections.defaultdict(list)
        memo[0] = [[]]
 
        for c in candidates:
            for t in range(c, target + 1):
                for res in memo[t-c]:
                    memo[t].append(res + [c])

        return memo[target]

    def combinationSum_DFS(self, candidates, target):
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0:
                return True # backtracking
            if target == 0:
                res.append(path)
                return False
            for i in range(index, len(candidates)):
                if dfs(target-candidates[i], i, path+[candidates[i]]): break
        
        dfs(target, 0, [])
        return res

    def removeStones(self, stones):
        return

    def permute(self, nums):
        stack = [(nums, [])]   # -- nums, path (or perms)
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                stack.append((newNums, path+[nums[i]]))  # --  just like we used to do (path + [node.val]) in tree traversal

        return res

sol = Solution()
print(sol.combinationSum([2,3,6,7],7))
