class Solution(object):
    def generateParenthesis(self, n):
        # stack keeps the current string of parentheses we're building
        stack = []
        # res stores all the valid results we find
        res = []

        def backtrack(openN, closedN):
            """
            openN   = number of '(' used so far
            closedN = number of ')' used so far
            """

            # Base case: if both open and close counts reach n,
            # it means we used up all parentheses properly.
            if openN == closedN == n:
                res.append("".join(stack))  # join stack into a string and save it
                return 

            # If we still have '(' left to use, slap one on the stack
            if openN < n:
                stack.append("(")              # choose
                backtrack(openN + 1, closedN)  # explore
                stack.pop()                    # undo (backtrack)

            # If we can add ')' without breaking the balance
            if closedN < openN:
                stack.append(")")              # choose
                backtrack(openN, closedN + 1)  # explore
                stack.pop()                    # undo

        # Kick off recursion starting with nothing
        backtrack(0, 0)
        return res


# ----------------- DEMO -----------------
if __name__ == "__main__":
    sol = Solution()
    n = 3
    result = sol.generateParenthesis(n)
    
    print(f"All well-formed parentheses for n={n}:")
    print(result)
