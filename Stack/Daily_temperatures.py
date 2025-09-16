class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Problem:
        You’re given an array 'temperatures' where each element represents the daily temperature.
        For each day, you need to figure out how many days you’ll have to wait until a warmer temperature shows up.
        If no warmer day exists in the future, put 0.

        Example:
        Input:  [73,74,75,71,69,72,76,73]
        Output: [1, 1, 4, 2, 1, 1, 0, 0]
        Why? 
        - On day 0 (73°F), the next warmer day is day 1 (74°F), so wait = 1
        - On day 1 (74°F), next warmer day is day 2 (75°F), so wait = 1
        - On day 2 (75°F), next warmer day is day 6 (76°F), so wait = 4
        - Keep going...
        """

        # Initialize result array with 0s (default: no warmer day ahead)
        res = [0] * len(temperatures)

        # Stack to keep track of temperatures we haven't resolved yet
        # Each element in stack = [temperature, index]
        stack = []

        # Loop through each day
        for i, t in enumerate(temperatures):
            # While there is something in the stack AND today’s temp is hotter 
            # than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # Pop that colder day
                # Calculate how many days it took to find a warmer day
                res[stackInd] = (i - stackInd)

            # Push current day onto stack (to wait for a warmer one later)
            stack.append([t, i])

        # Done looping, return result
        return res
