class Solution(object):
    def validateStackSequences(self, pushed, popped):
        i = 0  
        stack = []  
        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack


if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print("Example 1:", Solution().validateStackSequences(pushed, popped))  # True

    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print("Example 2:", Solution().validateStackSequences(pushed, popped))  # False
