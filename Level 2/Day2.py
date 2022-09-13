class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if '0' in [num1, num2]:
            return '0'

        result = [0] * (len(num1) + len(num2))

        for d1 in range(len(num1)):
            for d2 in range(len(num2)):
                product = int(num1[len(num1) - d1 -1]) * int(num2[len(num2) - d2 -1])
                
                result[d1+d2] += product
                result[d1+d2+1] += result[d1+d2]//10
                result[d1+d2] = result[d1+d2]%10

        result, zeros = result[::-1], 0

        while zeros < len(result) and result[zeros] != 0:
            zeros += 1

        result = map(str, result[zeros:])

        return ''.join(result)
        
                