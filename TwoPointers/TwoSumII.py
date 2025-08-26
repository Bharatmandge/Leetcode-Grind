"""
PROBLEM: Two Sum II - Input Array Is Sorted (LeetCode #167)

We’re given:
- A 1-indexed array of integers called `numbers`, sorted in non-decreasing order.
- A target value.

We need:
- Find two distinct numbers in `numbers` that add up to the target.
- Return their indices as [index1, index2], where index1 < index2.
- Indices are 1-based, not 0-based. (Yes, LeetCode loves making you off-by-one.)

Constraints:
- Exactly one solution exists. (No need to panic about multiple answers.)
- Must use constant extra space → meaning O(1) memory.
- Array is already sorted, so that’s a hint to avoid brute-force O(n^2).
"""

class Solution(object):
    def twoSum(self, numbers, target):
        # Initialize two pointers:
        # left starts at the beginning, right starts at the end.
        left, right = 0, len(numbers) - 1
        
        # Keep moving pointers until they meet
        while left < right:
            # Current sum of two pointers
            s = numbers[left] + numbers[right]
            
            # If sum matches the target, we found the answer
            if s == target:
                # +1 because the problem wants 1-based indexing
                return [left + 1, right + 1]
            
            # If sum is too small, move the left pointer to the right
            elif s < target:
                left += 1
                
            # If sum is too big, move the right pointer to the left
            else:
                right -= 1


"""
EXPLANATION OF THE SOLUTION:

Why two pointers? Because the array is already sorted.
- If the sum of numbers[left] + numbers[right] is too small, moving left forward increases the sum.
- If the sum is too large, moving right backward decreases the sum.
- This way, in one pass (O(n)) we can find the pair.

This satisfies the space constraint (constant extra space), 
and it’s efficient compared to the naive brute-force O(n^2).
"""
