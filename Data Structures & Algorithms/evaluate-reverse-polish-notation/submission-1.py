class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # one operator takes two arguments
        # stack numbers & if we reach an operator, pop two from the stack

        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                second = stack.pop()
                stack.append(stack.pop() - second)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                second = stack.pop()
                stack.append(int(stack.pop() / second))
            else:
                stack.append(int(t))
        
        return stack.pop()