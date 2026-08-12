class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l == 1: return False
        stack = []
        for i in range(l):
            if len(stack) != 0:
                top = len(stack)-1
                if s[i] == ']' and stack[top] == '[':
                    stack.pop()
                elif s[i] == '}' and stack[top] == '{':
                    stack.pop()
                elif s[i] == ')' and stack[top] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
                    continue
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        else:
            return True

