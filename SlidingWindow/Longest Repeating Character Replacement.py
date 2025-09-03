"""
424. Longest Repeating Character Replacement

QUESTION:
-----------
We are given:
- A string 's' consisting of uppercase English letters.
- An integer 'k' which represents how many characters we are allowed to change.

We can choose ANY character in the string and replace it with ANY uppercase letter.
We can do this at most 'k' times.

The goal:
---------
Find the length of the longest substring where, after performing at most 'k' changes,
all characters in that substring are the SAME letter.

Examples:
----------
1. s = "ABAB", k = 2
   - We can change both 'A's to 'B' (or both 'B's to 'A')
   - Longest substring of same letters = "BBBB" (length 4)

2. s = "AABABBA", k = 1
   - Change the middle 'A' to 'B'
   - Now substring "BBBB" has length 4
   - So answer is 4


SOLUTION IDEA:
---------------
We use the SLIDING WINDOW technique:
- We'll keep a window [l, r] that represents a substring of s.
- We keep track of how many times each character appears in the window (frequency map).
- max_count = the count of the most frequent character in the current window.
- If the window length minus max_count > k:
    -> It means we need more than 'k' changes to make the window all same letters.
    -> So, we shrink the window from the left.
- Otherwise, update the result with the current window length.

This works because:
- The key is that the limiting factor is the most frequent character in the window.
- The rest of the characters can potentially be replaced (using our 'k' operations).
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0                 # Left pointer of the sliding window
        freq = {}             # Dictionary to count frequency of characters in the window
        max_count = 0         # Maximum frequency of a single character in the window
        res = 0               # Final result (longest length found)

        # Expand the right pointer 'r' over the string
        for r in range(len(s)):
            # Count the frequency of the current character
            freq[s[r]] = freq.get(s[r], 0) + 1

            # Update the max frequency seen so far
            max_count = max(max_count, freq[s[r]])

            # If the window size minus max_count is bigger than k,
            # we can't make this window all the same character with <= k changes
            if (r - l + 1) - max_count > k:
                freq[s[l]] -= 1  # Remove the leftmost character from window
                l += 1           # Shrink the window

            # Update result with the size of the current valid window
            res = max(res, r - l + 1)

        return res


# -----------------
# DRIVER CODE TO TEST
# -----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))    # Expected output: 4
    print(sol.characterReplacement("AABABBA", 1)) # Expected output: 4
