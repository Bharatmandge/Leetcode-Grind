"""
Problem: Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time (O(1)).

Requirements:
- MinStack() -> initialize stack object
- push(val) -> push element onto stack
- pop() -> remove element from top
- top() -> return top element
- getMin() -> return minimum element in stack

Constraints:
- Values can range from -2^31 to (2^31 - 1)
- All operations should run in O(1)
- At most 3 * 10^4 operations will be called

Example:
----------
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); # returns -3
minStack.pop();
minStack.top();    # returns 0
minStack.getMin(); # returns -2
"""

class MinStack:
    def __init__(self):
        """
        Initialize two stacks:
        - stack: normal stack to store values
        - minStack: stores the minimum value at each level of the stack
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        """
        Pushes the element 'val' onto the stack.
        Also pushes the minimum value so far onto minStack.
        """
        self.stack.append(val)
        # If minStack is empty, val is the minimum
        # Otherwise, compare val with current min and push the smaller one
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        """
        Removes the top element from both stack and minStack.
        Ensures both remain in sync.
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        """
        Returns the top element of the stack.
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the current minimum element in the stack.
        """
        return self.minStack[-1]


# Example usage:
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Output: -3
    minStack.pop()
    print(minStack.top())     # Output: 0
    print(minStack.getMin())  # Output: -2
