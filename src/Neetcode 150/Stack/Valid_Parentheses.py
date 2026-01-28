class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False 
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
            
        return not stack
