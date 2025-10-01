
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    closeToOpen = { '}': '{', ']': '[', ')': '('}

    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False

s = "()[]{}" #should return false
x = "([)]" #should return false

print(isValid(s))