"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
            elif s[i] == ']':
                if len(stack) == 0:
                    return False
                elif stack.pop() != '[':
                    return False
            elif s[i] == '}':
                if len(stack) == 0:
                    return False
                elif stack.pop() != '{':
                    return False
            elif s[i] == ')':
                if len(stack) == 0:
                    return False
                elif stack.pop() != '(':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        