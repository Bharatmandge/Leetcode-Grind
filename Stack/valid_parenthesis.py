# Problem: Valid Parentheses
# You’re given a string 's' that only contains: '(', ')', '{', '}', '[' and ']'.
# You need to check if this string is "valid".
#
# A string is valid if:
# 1. Open brackets are closed by the SAME type of bracket.
# 2. Brackets are closed in the CORRECT order (no mismatches).
# 3. Every closing bracket has a corresponding opening bracket.
#
# Examples:
# "()"       -> True
# "()[]{}"   -> True
# "(]"       -> False
# "([])"     -> True
# "([)]"     -> False
#
# Constraints: 
# Length of string is between 1 and 10^4 (so we can’t brute force every possibility).
#
# Solution Approach: Use a STACK.
# Why stack? Because the last opened bracket must be closed first (LIFO order).
# Example: "([])" -> push '(' -> push '[' -> see ']' -> pop '[' -> see ')' -> pop '(' -> stack empty -> valid.

class Solution(object):
    def isValid(self, s):
        # stack will keep track of opening brackets
        stack = []
        
        # Map of closing bracket to its matching opening bracket
        closeToOpen = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        # Loop through every character in the string
        for c in s:
            # If it's a closing bracket
            if c in closeToOpen:
                # Check if stack has something and if top of stack matches
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # valid pair found -> pop the opening bracket
                else:
                    return False  # mismatch or empty stack -> invalid
            else:
                # It's an opening bracket -> push to stack
                stack.append(c)

        # After processing everything, stack should be empty if valid
        return not stack


# ------------------- Testing -------------------
obj = Solution()
print(obj.isValid("()"))       # True
print(obj.isValid("()[]{}"))   # True
print(obj.isValid("(]"))       # False
print(obj.isValid("([])"))     # True
print(obj.isValid("([)]"))     # False
  