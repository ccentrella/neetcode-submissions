class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # Continuously shift n until until it is 0
        # For each iteration, if last bit is 1, increment count
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            
            n = n >> 1

        return count