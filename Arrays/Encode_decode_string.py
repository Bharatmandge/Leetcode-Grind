"""
Problem:
---------
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

We need two functions:
1. encode(strs): converts list -> single string
2. decode(s): converts single string -> list

Why special encoding?
----------------------
If we simply join with ',' or '#', it breaks when those characters are inside the strings themselves.
So, we use a safe trick:
- Encode as: "length_of_string#string"
- Example: ["neet","code"] -> "4#neet4#code"
- While decoding, read the length first, then extract exactly that many characters.
"""

class Solution:

    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        """
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        """
        res, i = [], 0
        n = len(s)

        while i < n:
            # find position of '#'
            j = s.find('#', i)
            # extract length
            length = int(s[i:j])
            # extract the string
            start = j + 1
            end = start + length
            res.append(s[start:end])
            # move pointer forward
            i = end

        return res


# ----------------- Testing as per given examples -----------------

solution = Solution()

# Example 1
input1 = ["neet","code","love","you"]
print("Input:", input1)
print("Output:", solution.decode(solution.encode(input1)))

# Example 2
input2 = ["we","say",":","yes"]
print("\nInput:", input2)
print("Output:", solution.decode(solution.encode(input2)))
