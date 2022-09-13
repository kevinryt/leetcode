from curses.ascii import isdigit


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def true_returns(str):
            ans = []
            for char in str:
                if char != '#':
                    ans.append(char)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return true_returns(s) == true_returns(t)

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
        
        return ''.join(stack)