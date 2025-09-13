class Solution(object):
    def romanToInt(self, s):
        # Step 1: Create a mapping of Roman numerals to their integer values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Step 2: Initialize total result and a variable to keep track of the previous value
        total = 0
        prev = 0

        # Step 3: Loop through the Roman numeral string in reverse order
        # Why reverse? Because Roman numerals sometimes subtract smaller values from bigger ones (e.g., IV = 4).
        # By reversing, we can decide easily whether to add or subtract.
        for char in reversed(s):
            value = roman[char]  # Get the integer value of the Roman character
            
            # Step 4: If the current value is less than the previous value, subtract it
            # Example: In "IV", when we see "I" (1) after "V" (5), 1 < 5, so subtract -> total = 5 - 1 = 4
            if value < prev:
                total -= value
            else:
                # Step 5: Otherwise, just add the value
                # Example: In "VI", we see "I" (1) after "V" (5), 1 < 5 but in reverse order it's fine -> total = 5 + 1 = 6
                total += value
            
            # Step 6: Update the previous value for the next iteration
            prev = value
        
        # Step 7: Return the computed integer value
        return total
