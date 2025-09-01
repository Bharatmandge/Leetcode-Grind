class Solution:
    def maxProfit(self, prices):
        """
        The problem:
        You're given an array 'prices' where prices[i] = stock price on day i.
        You can only buy once and sell once (buy before sell).
        Goal: maximize profit (sell price - buy price).
        If profit can't be made, return 0.
        """

        # Step 1: Initialize the variables
        # min_price -> track the lowest price we've seen so far (buying opportunity)
        # max_profit -> track the highest profit possible so far
        min_price = float('inf')  # start with "infinity" so any price will be smaller
        max_profit = 0  # start with 0 profit

        # Step 2: Traverse the price list day by day
        for p in prices:
            # If current price is smaller than the min we've seen -> update min_price
            if p < min_price:
                min_price = p  # we found a better day to buy

            # Else, check if selling at this price gives us a bigger profit
            elif p - min_price > max_profit:
                max_profit = p - min_price  # update profit

        # Step 3: Return the max profit after scanning all days
        return max_profit
