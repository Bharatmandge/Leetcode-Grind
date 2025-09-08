from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Problem:
        You're given an array 'nums' and a window size 'k'.
        A window slides from left to right across 'nums'.
        At each step, we need to output the maximum element inside the window.

        Naive Approach:
        - For each window, scan all 'k' elements -> O(n * k)
        - Too slow when nums.length = 10^5 (will timeout)

        Optimized Approach:
        - Use a deque to keep track of useful indices.
        - Maintain it in decreasing order of values (front is always the max).
        - Time complexity: O(n) because each index is pushed/popped at most once.
        """

        output = []              # final result list
        q = deque()              # will store *indices* of nums, not values
        l = r = 0                # left and right pointers of window

        while r < len(nums):
            # Step 1: Maintain decreasing order in deque
            # If current num is bigger, kick out smaller ones from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)  # push current index

            # Step 2: Remove indices that are out of window
            if l > q[0]:
                q.popleft()

            # Step 3: When window size hits k, record the max
            if (r + 1) >= k:
                output.append(nums[q[0]])  # q[0] always stores index of max
                l += 1                     # move window’s left bound

            # Always move right pointer
            r += 1

        return output


# --------------------------
# Example run
# --------------------------
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(nums, k))  
# Expected: [3, 3, 5, 5, 6, 7]
