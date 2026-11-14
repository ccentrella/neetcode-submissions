class Solution:
    def climbStairs(self, n: int) -> int:
        # Same algorithm as fibonacci

        # One each stair we climb, we add up number of steps of last two existing,
        # since we can either go one step or two steps

        # At the beginning we only have one option
        second_last, last = 1, 1
        for _ in range(n):
            temp = last
            last = second_last + last
            second_last = temp

        return second_last