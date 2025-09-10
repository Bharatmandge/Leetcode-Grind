class Solution(object):
    def minimumDifference(self, nums, k):
        """
        Problem Explanation:
        --------------------
        We are given a list of student scores (nums) and a number k.
        We need to select k students from the list in such a way that:
            - The difference between the highest and lowest selected score is minimized.

        Example:
        nums = [9,4,1,7], k = 2
        Possible groups of 2 students:
            [9,4] -> max = 9, min = 4, difference = 5
            [9,1] -> difference = 8
            [9,7] -> difference = 2
            [4,1] -> difference = 3
            [7,4] -> difference = 3
            [7,1] -> difference = 6
        Minimum difference = 2 (when picking [9,7]).
        
        Goal: Find that minimum possible difference efficiently.
        """

        # Step 1: Sort the array
        # Why? Because the closest scores will always be near each other
        # after sorting. No need to compare distant elements unnecessarily.
        nums.sort()

        # Step 2: Initialize result as infinity
        # We'll try to minimize this value by checking valid groups of size k
        res = float('inf')

        # Step 3: Use a sliding window of size k
        # We only need to check consecutive groups of k elements after sorting
        # because the smallest range will be among them.
        for i in range(len(nums) - k + 1):
            # Calculate the difference between max and min in this window
            # Since array is sorted, max = nums[i + k - 1], min = nums[i]
            diff = nums[i + k - 1] - nums[i]

            # Update the result with the smaller difference
            res = min(res, diff)

        # Step 4: Return the minimum difference found
        return res


# Example usage:
solution = Solution()
print(solution.minimumDifference([9, 4, 1, 7], 2))  # Output: 2
print(solution.minimumDifference([90], 1))          # Output: 0
