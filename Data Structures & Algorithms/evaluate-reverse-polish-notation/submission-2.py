class Solution:
    operations = ['+','-','*','/']
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if e not in self.operations:
                stack.append(int(e))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                match e:
                    case '+':
                        stack.append(num1+num2)
                    case '-':
                        stack.append(num1-num2)
                    case '*':
                        stack.append(num1*num2)
                    case '/':
                        stack.append(int(num1/num2))

        return stack.pop()
        