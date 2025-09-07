# Problem: Fruit Into Baskets (LeetCode 904 - Medium)
# ---------------------------------------------------
# You are visiting a farm with a row of fruit trees, represented by an array `fruits`.
# Each element in `fruits` is the type of fruit a tree produces.
#
# Rules:
# 1. You have only 2 baskets.
# 2. Each basket can only hold ONE type of fruit (but unlimited quantity of that type).
# 3. You must pick exactly one fruit from every tree you pass, starting from any tree
#    and moving only to the right.
# 4. You must stop when you encounter a fruit type that doesn't fit into your 2 baskets.
#
# Goal: Find the maximum number of fruits you can pick while following these rules.
#
# Example:
# fruits = [1,2,1] → Output = 3 (you can take all)
# fruits = [0,1,2,2] → Output = 3 (best choice is [1,2,2])
# fruits = [1,2,3,2,2] → Output = 4 (best choice is [2,3,2,2])
#
# Constraint: 
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
#
# This is basically a "Longest Subarray with at Most 2 Distinct Numbers" problem.
# We solve it using the Sliding Window technique.

import collections

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        # count will store the frequency of each fruit type inside the window
        count = collections.defaultdict(int)

        # l = left pointer of sliding window
        # total = current window size (number of fruits collected)
        # res = maximum fruits collected so far
        l, total, res = 0, 0, 0

        # r = right pointer, iterate through all trees
        for r in range(len(fruits)):

            # include the current fruit in our basket (window)
            count[fruits[r]] += 1
            total += 1

            # If we have more than 2 types of fruits, shrink from the left
            while len(count) > 2:
                f = fruits[l]             # fruit at the left edge
                count[f] -= 1             # remove it from window
                total -= 1                # shrink window size
                l += 1                    # move left pointer forward

                # if no more of that fruit remains, drop it from dictionary
                if not count[f]:
                    count.pop(f)

            # update result with max window size so far
            res = max(res, total)

        return res


# Example Usage:
if __name__ == "__main__":
    obj = Solution()
    print(obj.totalFruit([1,2,1]))     # Output: 3
    print(obj.totalFruit([0,1,2,2]))   # Output: 3
    print(obj.totalFruit([1,2,3,2,2])) # Output: 4
