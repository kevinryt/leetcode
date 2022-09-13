from collections import defaultdict, deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        prereq_dic = { c:[] for c in range(numCourses)}

        for course, pre in prerequisites:
            prereq_dic[course].append(pre)

        output = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True

            cycle.add(course)

            for pre in prereq_dic[course]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output

    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        # This is a very good BFS problem.
        # In BFS, we need to traverse all positions in each level firstly, and then go to the next level.
        # Our task is to figure out:
        # 1. What is the level in this problem?
        # 2. What is the position we want in this problem?
        # 3. How to traverse all positions in a level?
        # 
        # For this problem:
        # 1. The level is each time to take bus.
        # 2. The position is all of the stops you can reach for taking one time of bus.
        # 3. Using a queue to record all of the stops can be arrived for each time you take buses.
        if source == target: return 0

        graph = defaultdict(list)

        # You need to record all the buses you can take at each stop so that you can find out all of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        for bus, stops in enumerate(routes):
            for stop in stops:
                graph[stop].append(bus)

        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([source])
        # Using visited to record the buses that have been taken before, because you needn't to take them again.
        visited = set()
        res = 0

        while queue:
            # take one time of bus.
            res += 1
            # In order to traverse all of the stops you can reach for this time, you have to traverse
            # all of the stops you can reach in last time.
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in graph[curStop]:
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target: return res
                        queue.append(stop)
        return -1