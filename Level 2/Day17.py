class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)           #for BC II and BC III
            if op == "/": stack.append(int(stack.pop() / v))      #for BC II and BC III
    
        i, num, stack, sign = 0, 0, [], "+"
        
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+-*/":
                update(sign, num)
                num, sign = 0, s[i]
            elif s[i] == "(":                                        # For BC I and BC III
                num, j = self.calculate(s[i + 1:])
                i = i + j
            elif s[i] == ")":                                        # For BC I and BC III
                update(sign, num)
                return sum(stack), i + 1
            i += 1
        update(sign, num)
        return sum(stack)
    def asteroidCollision(self, asteroids):
        right_ast, left_ast = [], []
        output = []

        for ast in asteroids:
            if ast > 0:
                right_ast.append(ast)
            else:
                left_ast.append(ast)


            while right_ast and left_ast:
                if right_ast[-1] > -left_ast[-1]:
                    left_ast.pop()
                elif right_ast[-1] < -left_ast[-1]:
                    right_ast.pop()
                else:
                    left_ast.pop()
                    right_ast.pop()
        if not right_ast and left_ast:
            output.append(left_ast.pop)

        return output + right_ast

sol = Solution()
print(sol.calculate("14-3/2"))