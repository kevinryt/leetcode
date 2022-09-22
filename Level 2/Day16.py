class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        output = []
        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                max(newInterval[1], intervals[i][1])]

        output.append(newInterval)

        return output

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for left,right in intervals[1:]:
            if output[-1][1] >= left:
                output[-1][1] = max(right,output[-1][1])
            else:
                output.append([left,right])

        return output

sol = Solution()
print(sol.insert([[1,3],[6,9]],[2,5]))