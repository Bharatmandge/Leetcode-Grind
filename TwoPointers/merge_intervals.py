"""
Leetcode 56: Merge Intervals
Problem:
Given a collection of intervals, merge all overlapping intervals.

Approach:
1. Sort intervals by start time.
2. Compare each interval with the last merged one.
3. Merge if overlapping, else add separately.
"""

class Solution(object):
    def merge(self, intervals):
        # Sort intervals by start time
        intervals.sort(key=lambda i: i[0])

        # Initialize result with the first interval
        output = [intervals[0]]

        # Iterate over the remaining intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:  # Overlap case
                output[-1][1] = max(lastEnd, end)  # Merge intervals
            else:  # No overlap
                output.append([start, end])

        return output


if __name__ == "__main__":
    # Example test cases
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(sol.merge([[1,4],[4,5]]))                  # [[1,5]]
    print(sol.merge([[4,7],[1,4]]))                  # [[1,7]]
