class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        O(n) time and space
        stack
        '''
        operators = {'/', '-', '*', '+'}
        stack = []
        for t in tokens:
            if t in operators:
                # pop twice -> num1, num2
                num2 = stack.pop()
                num1 = stack.pop()

                # perform op on numbers
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num1 - num2 
                elif t == '*':
                    res = num1 * num2
                else:
                    res = int(float(num1) / num2) # round to 0

                # add back to stack
                stack.append(res)
            # if num, append to stack
            else:
                stack.append(int(t))

        # return num in stack
        return stack[-1]
