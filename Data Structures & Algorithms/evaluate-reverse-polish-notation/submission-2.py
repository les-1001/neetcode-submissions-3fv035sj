class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ans = []

        for t in tokens:
            if t == "+":
                ans.append(ans.pop() + ans.pop())
            elif t == "*":
                ans.append(ans.pop() * ans.pop())
            elif t == "-":
                a, b = ans.pop(), ans.pop()
                ans.append(b - a)
            elif t == "/":
                a, b = ans.pop(), ans.pop()
                ans.append(int(b / a))
            else:
                ans.append(int(t))
        
        return ans[0]