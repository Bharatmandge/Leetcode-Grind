# Problem: Longest Harmonious Subsequence (LeetCode #594)
# 
# A "harmonious array" is defined as one where the difference between 
# the maximum and minimum values is exactly 1.
#
# Task:
# Given an integer array `nums`, return the length of the *longest harmonious subsequence*.
#
# Notes:
# - A subsequence does not need to be contiguous (order matters, but we can skip elements).
# - The key is finding two numbers that differ by exactly 1, 
#   then counting how many times they appear in total.
#
# Example:
# Input:  [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The subsequence [3,2,2,2,3] has max=3, min=2, and length=5.

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count how many times each number appears
        freq = Counter(nums)

        # Variable to track the longest harmonious subsequence length
        max_len = 0

        # Iterate through each unique number in the array
        for num in freq:
            # Check if there's a number exactly 1 greater
            if num + 1 in freq:
                # Combine counts of num and num+1
                max_len = max(max_len, freq[num] + freq[num + 1])
        
        # If no valid subsequence is found, this will stay 0
        return max_len
