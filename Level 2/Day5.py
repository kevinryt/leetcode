import collections

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_set = set(words)
        length = 0
        max_double = 0

        for word in words_set:
            if word == word[::-1] and words.count(word)%2 == 1:
                length += words.count(word)//2 * 2
                max_double = 1
            else:
                length += min(words.count(word[::-1]), words.count(word))

        return 2*(length + max_double)

    def longestPalindrome_counter(self, words):
        wc = collections.Counter(words)
        aa = 0  # count how many words contain only two identical letters like 'aa'
        center = 0  # if one count of 'aa' is odd, that means it can be the center of the palindrome, answer can plus 2
        abba = 0 # count how many word pairs like ('ab', 'ba') and they can put on both sides respectively

        for w, c in wc.items():
            if w[0] == w[1]: # like 'aa', 'bb', ...
                aa += c // 2 * 2 # if there are 3 'aa', we can only use 2 'aa' put on both sides respectively
                # if one count of 'aa' is odd, that means it can be the center of the palindrome, answer can plus 2
                if c % 2 == 1: center = 1
            else:
                abba += min(wc[w], wc[w[::-1]])  # will definitely double counting
        return 2 * (aa + int(abba) + center)

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # tasks = ["A","A","A","B","B","B"]
        # n = 2 
        
        counts = list(collections.Counter(tasks).values()) # [3,3]
        max_count = max(counts) # 3
        num_of_chars_with_max_count = counts.count(max_count) # 2, A and B
        
        num_of_chunks_with_idles = max_count-1 # 2  -> A  A  A

        # either a task will fill an empty place or the place stays idle, 
        # either way the chunk size stays the same  
        length_of_a_chunk_with_idle = n+1  # 3 -> A _ _ A _ _ A 

        # on the final chunk, there will only be most frequent letters 
        length_of_the_final_chunk = num_of_chars_with_max_count  # 2  

        length_of_all_chunks = (num_of_chunks_with_idles*length_of_a_chunk_with_idle) + length_of_the_final_chunk # 2*3 + 2 = 8 
        # -> A B _ A B _ A B 

        return max(len(tasks), length_of_all_chunks)


sol = Solution()
print(sol.longestPalindrome(["cc","ll","xx"]))