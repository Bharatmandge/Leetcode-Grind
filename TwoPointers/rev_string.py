# Problem:
# --------
# Given an input string s, we need to reverse the order of words.
# A word is defined as a sequence of non-space characters.
# The tricky part is:
#   - The string may have leading or trailing spaces.
#   - The string may contain multiple spaces between words.
#   - The final output must have exactly one space between words,
#     and no leading or trailing spaces.

# Example:
# Input:  "  hello world  "
# Output: "world hello"
#
# Input:  "a good   example"
# Output: "example good a"
#
# Input:  "the sky is blue"
# Output: "blue is sky the"

class Solution(object):
    def reverseWords(self, s):
        # Step 1: Remove leading and trailing spaces using strip()
        # Example: "  hello world  " --> "hello world"
        s = s.strip()
        
        # Step 2: Split the string into words using split()
        # By default, split() handles multiple spaces and treats them as one delimiter
        # Example: "a good   example" --> ["a", "good", "example"]
        words = s.split()
        
        # Step 3: Reverse the list of words
        # Example: ["a", "good", "example"] --> ["example", "good", "a"]
        words.reverse()
        
        # Step 4: Join the reversed list with a single space
        # Example: ["example", "good", "a"] --> "example good a"
        result = " ".join(words)
        
        # Return the final result
        return result


# ------------------------
# Testing the solution
# ------------------------
solution = Solution()

# Test case 1
print(solution.reverseWords("the sky is blue"))     # Output: "blue is sky the"

# Test case 2
print(solution.reverseWords("  hello world  "))     # Output: "world hello"

# Test case 3
print(solution.reverseWords("a good   example"))    # Output: "example good a"
