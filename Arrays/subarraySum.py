"""
PROBLEM EXPLANATION:

We are given:
- An integer array `nums`
- An integer `k`

We need to count how many **subarrays** (continuous slices of the array)
have a sum exactly equal to `k`.

Example 1:
nums = [1, 1, 1], k = 2
Possible subarrays:
[1], [1], [1], [1,1], [1,1], [1,1,1]
Sums are: 1, 1, 1, 2, 2, 3
There are exactly 2 subarrays with sum = 2 → Output = 2

Brute force way:
- Check all subarrays using 2 loops, calculate their sum, compare with k.
- Time complexity = O(n^2), which is too slow for large arrays.

Optimized way (used in this solution):
- Use a "prefix sum + hashmap" trick to achieve O(n).
"""

class Solution(object):
    def subarraySum(self, nums, k):
        prefixSum = 0        # running sum of elements seen so far
        count = 0            # total count of valid subarrays
        countMap = {0: 1}    # hashmap to store frequency of prefix sums
                             # initially {0:1} because if prefixSum == k at some point,
                             # we need to count that as one valid subarray.

        # iterate over all elements in nums
        for num in nums:
            prefixSum += num   # update the running prefix sum

            # KEY INSIGHT:
            # subarray(i...j) sum = prefixSum[j] - prefixSum[i-1]
            # => if (prefixSum - k) exists in countMap,
            # then there are subarrays ending here with sum == k
            if (prefixSum - k) in countMap:
                count += countMap[prefixSum - k]   # add all such possibilities

            # update countMap with the current prefixSum
            # (store how many times we've seen this sum so far)
            countMap[prefixSum] = countMap.get(prefixSum, 0) + 1

        return count          # return total number of valid subarrays
