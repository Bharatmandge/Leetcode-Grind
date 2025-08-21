"""
💡 Question:
Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive sequence 
of elements that can be formed.

👉 A consecutive sequence is a sequence of elements in which each element is 
exactly 1 greater than the previous element. 
👉 The elements do NOT have to be consecutive in the original array.

⚡ You must write an algorithm that runs in O(n) time.

---

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6].

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Step 1: Convert list into a set for O(1) lookups
        # Why? Because checking if a number exists in a set is much faster 
        # than checking in a list. This is crucial to achieve O(n) complexity.
        numbers = set(nums)

        # Step 2: Initialize the maximum length of longest consecutive sequence
        lengthLongestCon = 0

        # Step 3: Iterate through each number in the set
        for number in numbers:

            # Only start building a sequence if `number-1` is NOT in the set.
            # This ensures we always start at the beginning of a sequence.
            if (number - 1) not in numbers:
                tempLength = 1   # Current sequence length
                curr = number    # Start of sequence
            
                # Keep checking for the next consecutive numbers (curr+1, curr+2, ...)
                while curr + 1 in numbers:
                    tempLength += 1
                    curr += 1  # Move to next consecutive number
                
                # Update the longest sequence length found so far
                lengthLongestCon = max(lengthLongestCon, tempLength)

        # Step 4: Return the final answer
        return lengthLongestCon


# -------------------
# Testing the Solution
# -------------------
if __name__ == "__main__":
    obj = Solution()

    nums1 = [2,20,4,10,3,4,5]
    print("Input:", nums1)
    print("Longest Consecutive Sequence Length:", obj.longestConsecutive(nums1))  # Expected 4

    nums2 = [0,3,2,5,4,6,1,1]
    print("\nInput:", nums2)
    print("Longest Consecutive Sequence Length:", obj.longestConsecutive(nums2))  # Expected 7
