#Valid Parentheses
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    d = {"(":")", "[":"]", "{":"}"}
    stack = []

    if len(s) % 2 != 0:
        return False

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(d[char])
        else:
            if not stack or char != stack.pop():
                return False
    if stack:
        return False
    
    return True

print(isValid("){"))