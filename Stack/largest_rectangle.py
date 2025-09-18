class Solution(object):
    def largestRectangleArea(self, heights):
        """
        Problem:
        --------
        We are given a histogram represented as a list of bar heights. 
        Each bar has a width of 1. 
        We need to find the largest rectangular area that can be formed 
        inside this histogram.

        Example:
        --------
        Input: heights = [2,1,5,6,2,3]
        Visualization:
            |
            |        █ █
            |        █ █     █
            |  █     █ █     █
            |  █     █ █  █  █
            |  █  █  █ █  █  █
            ------------------------
               2  1  5  6  2  3

        Largest rectangle = height 5 (or 6) spanning over widths → area = 10.
        Output: 10
        """

        # maxArea will store the final answer (biggest rectangle found so far)
        maxArea = 0

        # stack will store pairs: (index, height)
        # The idea: maintain increasing heights in stack for processing efficiently
        stack = []

        # Step 1: Traverse through all bars
        for i, h in enumerate(heights):
            # By default, this bar "starts" at index i
            start = i

            # If the current bar is shorter than the bar on stack top,
            # then we can't extend the previous rectangle anymore.
            # So we pop from stack and calculate the max area with that popped height.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area: height * width
                # width = (current_index - index where popped height started)
                maxArea = max(maxArea, height * (i - index))
                # The new start point becomes the index of popped bar
                start = index

            # Push the current bar into stack with its valid start index
            stack.append((start, h))

        # Step 2: Clean up whatever is left in stack
        # Any heights left in stack can extend until the END of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


# ---------------------- DRIVER CODE ---------------------- #
# Example run
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(solution.largestRectangleArea([2,4]))          # Output: 4
