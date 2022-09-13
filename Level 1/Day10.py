class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def memory_fib(n, memo = {}):
            if n <= 1:
                return n
            try:
                return memo[n]
            except KeyError:
                result = memory_fib(n-2, memo) + memory_fib(n-1, memo)
                memo[n] = result
                return result

        return memory_fib(n)

    def fib_for_loop(self,n):
        if n <= 1:
            return n
        f1 = f2 = 1
        for i in range(2, n):
            f1, f2 = f2, f1 + f2
        return f2
        