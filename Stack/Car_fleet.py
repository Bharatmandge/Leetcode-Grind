"""
Car Fleet Problem:
-----------------
We are given cars at different starting positions and speeds.
Goal: Find how many car fleets will reach the target.

Key rules:
1. A car cannot pass another car in front of it.
2. If a faster car catches up with a slower car (or fleet), it becomes part of that fleet.
3. Fleets travel at the speed of the slowest car in that group.
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        # Step 1: Pair positions with speeds and sort by position in descending order
        # Why descending? Because we check cars from the one closest to target going backwards.
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0        # Count fleets formed
        prev_time = 0.0   # Time taken by last formed fleet to reach the target

        # Step 2: Iterate over cars
        for pos, spd in cars:
            # Time for current car to reach target
            time = (target - pos) / float(spd)

            # If current car takes longer, it forms a new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time   # Update latest fleet's arrival time

            # Else, this car joins the fleet ahead (no new fleet formed)

        return fleets


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # Expected: 3
    print(sol.carFleet(10, [3], [3]))                           # Expected: 1
    print(sol.carFleet(100, [0, 2, 4], [4, 2, 1]))              # Expected: 1
