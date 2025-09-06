# ===========================================
# Problem: 1652. Defuse the Bomb
# ===========================================

# You are given:
# - A circular array `code` of integers
# - An integer key `k`

# Task:
# Replace each element of the array with the sum of k other elements:
# 1. If k > 0: replace code[i] with sum of next k elements
# 2. If k < 0: replace code[i] with sum of previous |k| elements
# 3. If k == 0: replace code[i] with 0

# The array is circular, so after the last element it wraps back to the first, and vice versa.

# Example:
# code = [5,7,1,4], k = 3
# Output: [12, 10, 16, 13]
# Explanation:
# index 0 -> sum of next 3: 7+1+4 = 12
# index 1 -> sum of next 3: 1+4+5 = 10
# index 2 -> sum of next 3: 4+5+7 = 16
# index 3 -> sum of next 3: 5+7+1 = 13

# ===========================================
# Solution Using Sliding Window
# ===========================================

class Solution(object):
    def decrypt(self, code, k):
        N = len(code)            # Length of the circular array
        res = [0] * N            # Initialize result array with zeros

        # Special case: if k == 0, all elements become 0
        if k == 0:
            return res

        l = 0                    # Left pointer for sliding window
        cur_sum = 0              # Current sum of the window

        # We iterate through enough elements to cover the window size for all positions
        # Using modular arithmetic to handle the circular nature of the array
        for r in range(N + abs(k)):
            cur_sum += code[r % N]   # Add the rightmost element to the current sum

            # If the window is bigger than abs(k), slide the window forward
            if r - l + 1 > abs(k):
                cur_sum -= code[l % N]  # Remove the leftmost element from sum
                l += 1                   # Move left pointer forward

            # When window size equals abs(k), we assign sum to correct position
            if r - l + 1 == abs(k):
                if k > 0:
                    # For k > 0, sum of next k elements
                    # Assign sum to starting index of this window
                    res[(r - abs(k)) % N] = cur_sum
                else:
                    # For k < 0, sum of previous |k| elements
                    # Assign sum to the rightmost index of this window
                    res[(r + 1) % N] = cur_sum

        return res

# ===========================================
# Example Usage
# ===========================================

solution = Solution()

# Example 1
code = [5, 7, 1, 4]
k = 3
print("Example 1 Output:", solution.decrypt(code, k))  # Output: [12, 10, 16, 13]

# Example 2
code = [1, 2, 3, 4]
k = 0
print("Example 2 Output:", solution.decrypt(code, k))  # Output: [0, 0, 0, 0]

# Example 3
code = [2, 4, 9, 3]
k = -2
print("Example 3 Output:", solution.decrypt(code, k))  # Output: [12, 5, 6, 13]
