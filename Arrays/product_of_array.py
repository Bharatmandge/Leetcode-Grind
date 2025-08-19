# ---------------------------------------------------------
# 📝 Problem: Product of Array Except Self
# ---------------------------------------------------------
# Given an integer array nums, return an array output where
# output[i] is the product of all the elements of nums 
# except nums[i].
#
# Constraints:
# - Each product fits in a 32-bit integer.
# - Time: O(n)
# - No division allowed.
#
# Example 1:
# Input:  nums = [1,2,4,6]
# Output: [48,24,12,8]
#
# Example 2:
# Input:  nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]
#
# ---------------------------------------------------------
# 💡 Approach:
# - Use prefix and suffix products.
# - Prefix = product of all elements to the LEFT of index.
# - Suffix = product of all elements to the RIGHT of index.
# - Result[i] = Prefix[i] * Suffix[i].
#
# Implementation steps:
# 1. Create res[] initialized with 1s.
# 2. Forward pass → store prefix products.
# 3. Backward pass → multiply suffix products.
# 4. Return res.
# ---------------------------------------------------------

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n   # Step 1: Initialize result array with 1s

        # Step 2: Forward pass (build prefix products)
        prefix = 1
        for i in range(n):
            res[i] = prefix            # res[i] = product of all left elements
            prefix *= nums[i]          # update prefix with current number

        # Step 3: Backward pass (multiply suffix products)
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix           # multiply with product of right elements
            suffix *= nums[i]          # update suffix with current number

        # Step 4: Final result
        return res
