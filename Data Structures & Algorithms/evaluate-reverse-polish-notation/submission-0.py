class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if num add into stack
        # if +/* add/multiply last 2 num of stack in any order
        # if -// subtract/divide last num from 2nd last
        
        output = []

        for token in tokens:
            if token == "+":
                value = output.pop() + output.pop()
                output.append(value)
            elif token == "*":
                value = output.pop() * output.pop()
                output.append(value)
            elif token == "-":
                a = output.pop()
                b = output.pop()
                value = b - a
                output.append(value)
            elif token == "/":
                a = output.pop()
                b = output.pop()
                value = int(b / a)
                output.append(value)
            else:
                output.append(int(token))

        return output[0]