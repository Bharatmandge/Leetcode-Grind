class Solution:
    def threeSum(self, nums):
        # Step 1: Sort the array
        nums.sort()
        res = []  # to store the final triplets

        # Step 2: Fix one number (nums[i]) and use two pointers for the other two
        for i in range(len(nums)):
            # Skip duplicate values for nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue  

            left, right = i + 1, len(nums) - 1  # two-pointer setup

            # Step 3: Two-pointer search for pairs
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # Need a bigger sum → move left pointer
                    left += 1
                else:
                    # Need a smaller sum → move right pointer
                    right -= 1

        return res
   