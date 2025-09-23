class Solution(object):
    def find132pattern(self, nums):
        # stack will store pairs [nums[j], nums[i]] 
        # where nums[i] is the minimum value to the left of nums[j]
        stack = []
        
        # curMin keeps track of the minimum value encountered so far
        curMin = nums[0]

        # iterate through the array starting from the second element
        for n in nums[1:]:
            # pop elements from stack if the current number is greater
            # than or equal to the first element in the stack pair
            # This maintains stack[-1][0] as a candidate for '3' in '132'
            while stack and n >= stack[-1][0]:
                stack.pop()

            # check if current number can be the '2' in '132'
            # stack[-1][1] is the '1' in '132', stack[-1][0] is the '3'
            if stack and n > stack[-1][1]:
                return True  # found the pattern nums[i] < nums[k] < nums[j]

            # push the current number and the minimum so far to stack
            # n -> potential '3', curMin -> potential '1'
            stack.append([n, curMin])

            # update curMin with the minimum value seen so far
            curMin = min(curMin, n)

        return False  # if loop ends, no 132 pattern was found
