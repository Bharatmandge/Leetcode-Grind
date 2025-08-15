"""
Problem: Valid Anagram
--------------------------------
Given two strings s and t, return True if the two strings are anagrams of each other, otherwise return False.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: True

Example 2:
Input: s = "jar", t = "jam"
Output: False

Constraints:
- s and t consist of lowercase English letters.
- 1 <= len(s), len(t) <= 5 * 10^4

Approach:
--------------------------------
1. If the lengths of s and t are different, they cannot be anagrams.
2. Use a dictionary (hashmap) to store character frequencies of s.
3. Iterate through t, decreasing the frequency for each character.
4. If any character in t is not found in the hashmap or its frequency is zero, return False.
5. If all checks pass, return True.

Time Complexity: O(n) where n is the length of s or t
Space Complexity: O(1) because we only store at most 26 lowercase letters
"""

class Solution(object):
    def isAnagram(self, s, t):
        # Step 1: If lengths don't match, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Step 2: Dictionary to store frequency of each character in s
        count = {}

        # Step 3: Count frequency of each char in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1  # Increment count for each character

        # Step 4: Decrease frequency for each char in t
        for ch in t:
            # If char not found or frequency is 0, not an anagram
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1  # Reduce count for matching character

        # Step 5: If all checks pass, it's an anagram
        return True
