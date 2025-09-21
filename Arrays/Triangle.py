# File: min_triangle_path.py

class Solution:
    def minimumTotal(self, triangle):
        """
        Given a triangle array, return the minimum path sum from top to bottom.
        At each step, you may move to adjacent numbers on the row below.

        Approach:
        - Use dynamic programming (bottom-up).
        - Start from the last row and move upward.
        - dp[i] stores the minimum path sum starting from the current row to the bottom at index i.
        - For each element, we add its value to the minimum of the two elements directly below it in the DP array.
        """

        # Initialize dp array with extra space to avoid index errors
        dp = [0] * (len(triangle) + 1)

        # Start from the last row and move upwards
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                # For current element, take min of two paths below and add current value
                dp[i] = n + min(dp[i], dp[i+1])

        # dp[0] now contains the minimum path sum from top to bottom
        return dp[0]


if __name__ == "__main__":
    # Example 1
    triangle1 = [[2], [3,4], [6,5,7], [4,1,8,3]]
    sol = Solution()
    print("Minimum path sum for triangle1:", sol.minimumTotal(triangle1))  # Output: 11

    # Example 2
    triangle2 = [[-10]]
    print("Minimum path sum for triangle2:", sol.minimumTotal(triangle2))  # Output: -10
