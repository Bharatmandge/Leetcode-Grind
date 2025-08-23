"""
Problem: 205. Isomorphic Strings

Description:
------------
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`. 
- Every occurrence of a character must be replaced with another character consistently.
- The mapping must preserve the order of characters.
- No two characters can map to the same character, but a character may map to itself.

Examples:
----------
Example 1:
    Input: s = "egg", t = "add"
    Output: true
    Explanation: 'e' → 'a', 'g' → 'd'. 

Example 2:
    Input: s = "foo", t = "bar"
    Output: false
    Explanation: 'o' would need to map to both 'a' and 'r', which is invalid.

Example 3:
    Input: s = "paper", t = "title"
    Output: true
    Explanation: 'p' → 't', 'a' → 'i', 'e' → 'l', 'r' → 'e'.

Approach:
----------
We use two hashmaps (dictionaries in Python):
1. `hashmap_s` to track mapping from characters in `s` to characters in `t`.
2. `hashmap_t` to track mapping from characters in `t` back to characters in `s`.

While iterating through the strings:
- If a mapping already exists, check for consistency.
- If inconsistent, return False immediately.
- Otherwise, create the mapping in both hashmaps.

If no conflicts are found, the strings are isomorphic → return True.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if c1 in hashmap_s:
                if hashmap_s[c1] != c2:
                    return False

            if c2 in hashmap_t:
                if hashmap_t[c2] != c1:
                    return False

            hashmap_s[c1] = c2
            hashmap_t[c2] = c1

        return True


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))    # True
    print(sol.isIsomorphic("foo", "bar"))    # False
    print(sol.isIsomorphic("paper", "title")) # True
