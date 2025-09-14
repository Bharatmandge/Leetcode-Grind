# Problem: Evaluate Reverse Polish Notation (RPN)
# Example: ["2", "1", "+", "3", "*"] = (2 + 1) * 3 = 9
# Allowed operators: +, -, *, /
# Trick: Division must truncate toward ZERO, not floor like Python's //

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c == "+":
                # Normal addition
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Careful with subtraction: order matters
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # Multiplication, easy
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                # Here's the tricky part:
                # Python's // floors toward negative infinity, e.g. -3//2 = -2
                # But RPN problem wants truncate toward ZERO: -3/2 = -1
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))  # hack: cast to float, then int
            else:
                # If it's not an operator, it's a number
                stack.append(int(c))
        return stack[0]


# ------------------ DEMO ------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Normal case, no negatives
    expr1 = ["4","13","5","/","+"]
    # 13/5 = 2 (truncate toward 0), so 4 + 2 = 6
    print("Expression 1 result:", sol.evalRPN(expr1))  # Expected 6
    
    # Edge case with negatives
    expr2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # Ugly long example from LeetCode, expected result = 22
    print("Expression 2 result:", sol.evalRPN(expr2))  # Expected 22
    
    # Division check with negative numbers
    expr3 = ["-3","2","/"]
    # -3/2 should be -1 (truncate toward zero), not -2
    print("Expression 3 result:", sol.evalRPN(expr3))  # Expected -1
