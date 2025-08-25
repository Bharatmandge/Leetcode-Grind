# Problem: Valid Palindrome
# ---------------------------------
# Given a string s, return True if it is a palindrome, otherwise return False.
#
# A palindrome is a string that reads the same forward and backward.
# - It should be case-insensitive (ignores uppercase vs lowercase).
# - It should ignore all non-alphanumeric characters (spaces, punctuation, etc.).
#
# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: True
# Explanation: After filtering and lowering -> "wasitacaroracatisaw", which is a palindrome.
#
# Example 2:
# Input: s = "tab a cat"
# Output: False
# Explanation: After filtering and lowering -> "tabacat", which is not a palindrome.
#
# Constraints:
# - 1 <= s.length <= 1000
# - s consists of only printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one starting at the beginning,
        # the other at the end of the string.
        left, right = 0, len(s) - 1

        # Keep checking until the two pointers meet
        while left < right:

            # Move the left pointer forward if it's not an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move the right pointer backward if it's not an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters in lowercase to ignore case differences
            if s[left].lower() != s[right].lower():
                return False  # If mismatch, it's not a palindrome

            # Move both pointers towards the center
            left += 1
            right -= 1

        # If loop completes without mismatches, it's a palindrome
        return True
  