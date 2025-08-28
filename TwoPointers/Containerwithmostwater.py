# Problem: Container With Most Water
# ---------------------------------
# You are given an integer array `heights` where each element represents 
# the height of a vertical line on the x-axis. The goal is to pick two lines 
# that, together with the x-axis, form a container that can hold the maximum 
# amount of water.
#
# Formula:
#   Water stored between two lines = (distance between them) * (minimum of their heights)
#
# Example:
#   Input:  [1,7,2,5,4,7,3,6]
#   Output: 36
#
# Explanation: The max water is stored between height[1] = 7 and height[7] = 6.
#   Area = min(7, 6) * (7 - 1) = 6 * 6 = 36

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Left and right pointers (start and end of array)
        l, r = 0, len(heights) - 1
        
        # Variable to keep track of maximum water area
        res = 0
        
        # Move the pointers inward until they meet
        while l < r:
            # Height is determined by the shorter line
            # Width is the distance between lines
            area = min(heights[l], heights[r]) * (r - l)
            
            # Update result if this area is larger
            res = max(res, area)
            
            # Move the pointer that points to the shorter line
            # Why? Because moving the taller one won't help;
            # the height bottleneck stays the same or worse.
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        # Return the maximum water found
        return res


# ---------------------------
# Let's test it with examples
# ---------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.maxArea([1,7,2,5,4,7,3,6]))  # Expected output: 36
    
    # Example 2
    print(sol.maxArea([2,2,2]))  # Expected output: 4
