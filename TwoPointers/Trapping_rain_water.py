# Problem: Trapping Rain Water
#
# You are given an array "height" where each element represents
# the height of a vertical bar (like a histogram).
#
# When rain falls, water gets trapped between the taller bars
# if there are dips in between.
#
# Task: Find the TOTAL amount of trapped water.
#
# Example:
# height = [0,2,0,3,1,0,1,3,2,1]
#
# Visual representation:
#
#       |          
#   |   |       |  
#   |   |   |   | |  
#   |   |   |   | |  
# ---------------------
#  0 2 0 3 1 0 1 3 2 1
#
# Water fills the dips. Add it up → total = 9 units.
from collections import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # If the array is empty, no bars = no water
        if not height:
            return 0

        n = len(height)   # total number of bars
        res = 0           # result variable to store total trapped water

        # Iterate over every bar to calculate water trapped at that bar
        for i in range(n):
            # Start with the current bar height as the max
            leftMax = rightMax = height[i]

            # Step 1: find the tallest bar to the LEFT of index i
            for j in range(i):
                leftMax = max(leftMax, height[j])

            # Step 2: find the tallest bar to the RIGHT of index i
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            # Step 3: trapped water at bar i =
            # minimum of (highest bar to left, highest bar to right)
            # minus the height of current bar
            res += min(leftMax, rightMax) - height[i]

        # Return total trapped water after checking all bars
        return res
