class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem: Find the length of the longest substring with all unique characters.
        Idea: Use sliding window with two pointers (l, r).
              Expand r to include new characters.
              If a duplicate appears, shrink from l until window is valid again.
        """

        # A set to hold the characters currently inside our window.
        charSet = set()

        # Left boundary of the window
        l = 0

        # Store the maximum length found
        res = 0

        # Iterate with r = right boundary of window
        for r in range(len(s)):
            # If s[r] is already in the window, we have a duplicate.
            # Keep removing from the left until that duplicate disappears.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1  # Shrink from the left

            # Now s[r] is unique in the window, add it
            charSet.add(s[r])

            # Update max length (r - l + 1 is window size)
            res = max(res, r - l + 1)

        return res
