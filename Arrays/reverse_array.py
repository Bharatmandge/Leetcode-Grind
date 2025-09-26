"""
LeetCode Problem: Rotate Array
--------------------------------
You are given an array 'nums' and an integer 'k'.
Rotate the array to the right by 'k' steps.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Think of it like shifting everything to the right, and the elements
that fall off the end come back around to the front.
"""

# ------------------- BRUTE FORCE SOLUTION -------------------
# Time complexity: O(n * k) -> slow as hell for big arrays
# Idea: Do one step rotation, repeat it k times.
def rotate_bruteforce(nums, k):
    n = len(nums)
    k = k % n  # normalize k (because rotating n times = same array)

    for _ in range(k):
        # Pop last element and insert at front
        last = nums.pop()
        nums.insert(0, last)
    return nums


# ------------------- SMART SOLUTION (REVERSAL METHOD) -------------------
# Time complexity: O(n)
# Space complexity: O(1)
# Idea: Use array reversal trick:
#   1. Reverse entire array
#   2. Reverse first k elements
#   3. Reverse the rest
def rotate(nums, k):
    n = len(nums)
    k = k % n  # normalize k

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: reverse the whole array
    reverse(0, n - 1)
    # Step 2: reverse first k elements
    reverse(0, k - 1)
    # Step 3: reverse the rest
    reverse(k, n - 1)
    return nums


# ------------------- TESTING -------------------
arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = arr1[:]  # copy for second method

print("Original:", arr1)
print("Brute Force Rotate by 3:", rotate_bruteforce(arr1, 3))
print("Reversal Rotate by 3:   ", rotate(arr2, 3))
