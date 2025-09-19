# Problem:
# We have a row of asteroids represented as integers in an array.
# - Absolute value = size of the asteroid
# - Sign = direction of movement (positive = right, negative = left)
# Rule: 
#  - If two asteroids collide:
#       smaller one explodes,
#       if equal size -> both explode,
#       if moving in the same direction -> no collision.
# Goal: Return the final state of asteroids after all collisions.

class Solution(object):
    def asteroidCollision(self, asteroids):
        # We'll use a stack to simulate the asteroid field.
        # Why a stack? Because collisions only happen with the "latest asteroid in the line".
        stack = []

        # Go through each asteroid one by one
        for a in asteroids:
            # Condition for collision:
            # stack[-1] > 0  -> asteroid on the stack is moving right
            # a < 0          -> current asteroid is moving left
            # Only then they can meet each other.
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]  # Compare their sizes
                if diff < 0:
                    # Case 1: Incoming asteroid (a) is bigger in size (|a| > stack[-1])
                    # -> Pop the smaller asteroid from stack and check again
                    stack.pop()
                elif diff > 0:
                    # Case 2: Asteroid on stack is bigger (stack[-1] > |a|)
                    # -> Incoming asteroid dies, set a=0 to ignore it
                    a = 0
                else:
                    # Case 3: Equal size (|a| == stack[-1])
                    # -> Both explode, so pop stack asteroid and ignore incoming one
                    a = 0
                    stack.pop()

            # If after all that a still exists (not exploded), push it onto stack
            if a:
                stack.append(a)

        # Whatever survives in stack is the final state of the asteroid field
        return stack


# Example usage:
s = Solution()
print(s.asteroidCollision([5, 10, -5]))  # Output: [5, 10]
print(s.asteroidCollision([8, -8]))      # Output: []
print(s.asteroidCollision([10, 2, -5]))  # Output: [10]
