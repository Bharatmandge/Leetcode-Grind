class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Problem Recap:
        -----------------
        We are given two strings:
            s = the main string we search inside
            t = the string of characters we must include (with duplicates) in our window

        Goal:
        ------
        Find the smallest substring of 's' that contains all characters of 't'.
        If no such substring exists, return "".

        Example:
        s = "OUZODYXAZV", t = "XYZ"
        Answer: "YXAZ" (shortest substring containing 'X', 'Y', 'Z')
        
        Key Notes:
        -----------
        - We must include duplicates too. If t = "AABC", the substring must have 2 'A's, 1 'B', and 1 'C'.
        - Output is always unique as per problem statement.
        - Constraint sizes (up to 1000) let us use O(n) or O(n log n) solutions.
        
        Approach:
        ----------
        Sliding Window Technique + Hashmaps (Frequency Counters)
        1. Count frequency of characters in t (target requirements).
        2. Expand the right pointer (r) to include characters into the current window.
        3. Keep track of how many required characters are currently satisfied.
        4. When all are satisfied, try to shrink the window from the left (l) to get the minimum size.
        5. Track the best (smallest) window seen so far.
        """

        # Edge case: if t is empty, no substring is needed
        if t == "":
            return ""

        # Step 1: Count characters in t (requirements)
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 'have' = how many unique characters currently satisfied
        # 'need' = total unique characters required (from countT)
        have, need = 0, len(countT)

        # Result tracking: (left index, right index), and window length
        res, resLen = [-1, -1], float("inf")
        l = 0  # Left pointer of sliding window

        # Step 2: Expand the window with right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Step 3: Check if this character fulfills a requirement
            if c in countT and window[c] == countT[c]:
                have += 1

            # Step 4: When all requirements are satisfied, shrink from left
            while have == need:
                # Update result if this window is smaller than previous best
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # Shrink window from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1  # We no longer satisfy this character
                l += 1  # Move left pointer forward

        # Step 5: Return result substring if found, else ""
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
