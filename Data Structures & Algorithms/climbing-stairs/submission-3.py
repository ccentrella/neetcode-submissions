class Solution:
    def climbStairs(self, n: int) -> int:
        # Each time, we can climb either one step or two steps

        # From a given stair, either we climbed from the last step or from the second last, so add the last two numbers

        # Once we have climbed n - 1 steps, we will be in the right position
        # n - 1 because we have two separate variables we are moving

        # We don't need a check here, because given the base case, the loop will simply not execute and we will return 1

        second_last, last = 1, 1
        for _ in range(n - 1):
            temp = second_last + last
            second_last = last
            last = temp

        return last
