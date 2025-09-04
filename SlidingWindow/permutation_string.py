class Solution:
    def checkInclusion(self, s1, s2):
        # If s1 is longer than s2, no chance in hell we can find it
        if len(s1) > len(s2):
            return False

        # Frequency counters for characters 'a' to 'z'
        s1_count = [0] * 26  # store frequency of chars in s1
        s2_count = [0] * 26  # store frequency of current window in s2

        # Fill s1_count with char frequencies of s1
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        # Initialize the first window of s2 with same length as s1
        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1

        # If first window itself matches -> found permutation
        if s1_count == s2_count:
            return True

        # Now slide the window across s2
        for i in range(len(s1), len(s2)):
            # include new character in window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # remove the oldest character from window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Check after each shift if counts match
            if s1_count == s2_count:
                return True

        # If no window matched, then no permutation found
        return False
