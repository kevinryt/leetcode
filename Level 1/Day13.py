from collections import defaultdict
from email.policy import default
from sys import intern


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Hash_map = {}

        for i, n in enumerate(nums):
            if target - n in Hash_map:
                return [Hash_map[target - n], i]
            Hash_map[n] = i
        
        return

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cows = 0
        bulls = 0
        secret_count = defaultdict(int)
        guess_count = defaultdict(int)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cows += 1
            else:
                secret_count[secret[i]] += 1
                guess_count[guess[i]] += 1

        for j in guess_count:
            if j in secret_count:
                bulls += min(secret_count[j], guess_count[j])

        return str(cows)+'A'+str(bulls)+'B'