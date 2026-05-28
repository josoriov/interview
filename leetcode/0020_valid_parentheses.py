"""
LeetCode 20. Valid Parentheses

Approach:
- Use a stack and a mapping from closing to opening brackets.
- Iterate through the string: push opening brackets onto the stack.
- When a closing bracket is encountered, check that the stack is
  non-empty and that the top of the stack is the matching opener.
- After processing all characters the stack must be empty.

Time: O(n)
Space: O(n)
"""


def isValid(s: str) -> bool:
    opening = ["(", "{", "["]
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    for sub in s:
        if sub in opening:
            stack.append(sub)
        else:
            if not stack:
                return False
            elif mapping[sub] == stack[-1]:
                _ = stack.pop()
            else:
                return False
    return not stack

