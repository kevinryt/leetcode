from collections import defaultdict
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            new_stone = stones[-1] - stones[-2]
            stones = stones[:-2]
            
            if new_stone > 0:
                stones.append(new_stone)

        stones.append(0)
        return stones[0]
                
    def lastStoneWeight_heap(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop()
            second = heapq.heappop()

            if first < second:
                heapq.heappush(first - second)
            
        stones.append(0)
        return stones[0]

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        d = dict(sorted(word_count.items(), key=lambda item: (-item[1], item[0]))[0:k])
        
        return_list = []
        for name,_ in d.items():
            return_list.append(name)
        
        return return_list

sol = Solution()
print(sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
