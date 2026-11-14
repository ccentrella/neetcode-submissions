class Solution:
    def climbStairs(self, n: int) -> int:
        # Same algorithm as fibonacci

        # One each stair we climb, we add up number of steps of last two existing,
        # since we can either go one step or two steps

        # At the beginning we only have one option
        last, second_last = 1, 1
        for _ in range(n - 1):
            temp = last
            last = second_last + last
            second_last = temp

        return last