class Solution(object):
    def calPoints(self, operations):
        # We’ll use a stack (list) to keep track of the valid scores
        stack = []

        # Go through each operation in the input
        for op in operations:
            if op == "C":
                # "C" means cancel the last score -> pop the last element off the stack
                stack.pop()
            elif op == "D":
                # "D" means double the last score -> take the top of the stack and double it
                stack.append(2 * stack[-1])
            elif op == "+":
                # "+" means add the last two scores -> sum the last two stack elements
                stack.append(stack[-1] + stack[-2])
            else:
                # Otherwise, it must be a number (score)
                # Convert it from string to int and push it onto the stack
                stack.append(int(op))

        # Return the sum of all valid scores left in the stack
        return sum(stack)


# Example usage:
# Input: ["5","2","C","D","+"]
# Process:
#  -> push 5  => stack = [5]
#  -> push 2  => stack = [5, 2]
#  -> "C"     => remove last => stack = [5]
#  -> "D"     => double last => stack = [5, 10]
#  -> "+"     => add last two => stack = [5, 10, 15]
# Final stack = [5, 10, 15]
# Sum = 30
solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))  # Output: 30
