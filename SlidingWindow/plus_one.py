"""
LeetCode Problem: Plus One
Given a non-empty array of decimal digits representing a non-negative integer,
increment the integer by one and return the resulting array of digits.

We’ll show two solutions:
1. The readable iterative solution (clean and efficient).
2. The “one-liner flex” solution (converts to int, adds 1, converts back).
"""

class Solution:
    def plusOne_iterative(self, digits):
        """
        Iterative solution (real programmers' choice).
        Time complexity: O(n)
        
        Steps:
        - Start from the last digit (end of list).
        - If it's not 9, just increment and return.
        - If it is 9, turn it into 0 and carry over to the next digit.
        - If all were 9s, then add an extra 1 at the beginning.
        """
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # reset current digit to 0 if it was 9
        
        # Edge case: all digits were 9
        return [1] + digits

    def plusOne_oneliner(self, digits):
        """
        Python one-liner flex solution (not space-efficient but fun).
        Time complexity: O(n)
        
        Steps:
        - Convert the list of digits into a string.
        - Turn that string into an integer.
        - Add 1 to the integer.
        - Convert it back into a list of digits.
        """
        return [int(x) for x in str(int("".join(map(str, digits))) + 1)]


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    print("Iterative solution:")
    print(sol.plusOne_iterative([1, 2, 3]))  # [1, 2, 4]
    print(sol.plusOne_iterative([9, 9, 9]))  # [1, 0, 0, 0]
    
    print("\nOne-liner solution:")
    print(sol.plusOne_oneliner([1, 2, 3]))  # [1, 2, 4]
    print(sol.plusOne_oneliner([9, 9, 9]))  # [1, 0, 0, 0]
