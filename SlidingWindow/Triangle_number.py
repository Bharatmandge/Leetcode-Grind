class Solution(object):
    def triangleNumber(self, nums):
        # Step 1: Sort the array
        # Why? Because for triangle inequality (a + b > c),
        # if nums[k] is the largest side, we only need to check nums[i] + nums[j] > nums[k].
        nums.sort()
        
        N = len(nums)
        output = 0  # This will hold the total count of valid triangles

        # Step 2: Fix the largest side (nums[k]) and use two pointers for the smaller sides
        for k in range(2, N):  # Start from index 2 (since we need at least 3 sides)
            i, j = 0, k - 1   # i = start, j = just before k

            # Step 3: Two-pointer search
            while i < j:
                # If nums[i] + nums[j] > nums[k], it's a valid triangle
                if nums[i] + nums[j] > nums[k]:
                    # All pairs (i...j-1, j, k) will also be valid
                    # Because array is sorted, and nums[i+1] >= nums[i]
                    output += (j - i)
                    j -= 1  # Decrease j to check for other possible pairs
                else:
                    # If it's not valid, increase i to get a bigger sum
                    i += 1

        return output


# Example usage:
solution = Solution()
print(solution.triangleNumber([2, 2, 3, 4]))  # Output: 3
print(solution.triangleNumber([4, 2, 3, 4]))  # Output: 4
