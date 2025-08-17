"""
QUESTION:
---------
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, number of unique elements in nums]
- It is guaranteed that the answer is unique
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency of each number using hashmap
        count = {}
        # freq[i] will store list of numbers that appear exactly i times
        freq = [[] for _ in range(len(nums) + 1)]

        # Count frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Put numbers into their corresponding frequency bucket
        for n, c in count.items():
            freq[c].append(n)

        # Step 2: Collect top k frequent numbers
        res = []
        # Traverse frequencies in reverse (from high to low)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # If we already have k elements, return result
                if len(res) == k:
                    return res
