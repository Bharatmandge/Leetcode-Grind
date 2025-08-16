"""
Question:
-----------
Group Anagrams

Problem Statement:
-------------------
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An anagram is a word formed by rearranging the letters of another word, 
using all the original letters exactly once.

Example:
---------
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
-------------
- "eat", "tea", and "ate" are all anagrams of each other
  because they use the exact same letters ['a', 'e', 't'].
- "tan" and "nat" are anagrams of each other ['a', 'n', 't'].
- "bat" has no partner, so it forms its own group.

--------------------------------------------------------------------------------
"""

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        Function to group anagrams together.

        Args:
            strs (List[str]): List of input words (strings).

        Returns:
            List[List[str]]: List of groups, 
                             where each group contains words that are anagrams.
        """

        # Step 1: Create a dictionary (defaultdict of list)
        # Why defaultdict(list)? 
        # Because for every new key, it will automatically create an empty list,
        # so we can directly append words to it without worrying about 
        # checking if the key exists or not.
        sorted_groups = defaultdict(list)

        # Step 2: Loop through each word in the input list
        for word in strs:

            # Step 2.1: Sort the characters of the word
            # Example: "eat" -> ['a', 'e', 't'] -> "aet"
            # Example: "tea" -> ['a', 'e', 't'] -> "aet"
            # Both give the same sorted key -> "aet"
            key = "".join(sorted(word))

            # Step 2.2: Use the sorted word as a key in the dictionary
            # Append the original word to the group of its key
            sorted_groups[key].append(word)

        # Step 3: Convert dictionary values into a list
        # Example: {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}
        # Final Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        return list(sorted_groups.values())



# -----------------------------
# Example usage / Testing
# -----------------------------
if __name__ == "__main__":
    obj = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(strs))
    # Expected Output (order may vary):
    # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
