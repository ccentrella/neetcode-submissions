class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = 1 & (n >> i)
            result = result | (bit << (31 - i))

        return result