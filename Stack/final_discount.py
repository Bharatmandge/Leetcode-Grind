"""
Problem: Final Prices With a Special Discount in a Shop
LeetCode 1475

We are given an array `prices` where prices[i] is the price of the i-th item.
If you buy the i-th item, you receive a discount equal to the first future item
with price <= prices[i]. If no such item exists, you get no discount.

We need to return the final prices after discount.
"""

class Solution(object):

    def finalPrices_bruteforce(self, prices):
        """
        Brute Force Solution (O(n^2))
        ---------------------------------
        For each item, look ahead in the array to find
        the first smaller or equal item.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(prices)
        res = prices[:]
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    res[i] -= prices[j]
                    break  # stop at the first discount
        return res


    def finalPrices_stack(self, prices):
        """
        Optimized Solution using Monotonic Stack (O(n))
        ------------------------------------------------
        We use a stack to keep track of indices whose discounts 
        we haven't found yet. As soon as we encounter a price 
        smaller or equal, that becomes the discount for the 
        top of the stack.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        res = prices[:]

        for i, price in enumerate(prices):
            # Resolve discounts for items on the stack
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                res[idx] -= price
            # Add current index to stack
            stack.append(i)

        return res


# Example usage
if __name__ == "__main__":
    s = Solution()

    prices1 = [8, 4, 6, 2, 3]
    print("Brute Force:", s.finalPrices_bruteforce(prices1))  # [4, 2, 4, 2, 3]
    print("Stack Optimized:", s.finalPrices_stack(prices1))   # [4, 2, 4, 2, 3]

    prices2 = [1, 2, 3, 4, 5]
    print("Brute Force:", s.finalPrices_bruteforce(prices2))  # [1, 2, 3, 4, 5]
    print("Stack Optimized:", s.finalPrices_stack(prices2))   # [1, 2, 3, 4, 5]

    prices3 = [10, 1, 1, 6]
    print("Brute Force:", s.finalPrices_bruteforce(prices3))  # [9, 0, 1, 6]
    print("Stack Optimized:", s.finalPrices_stack(prices3))   # [9, 0, 1, 6]
