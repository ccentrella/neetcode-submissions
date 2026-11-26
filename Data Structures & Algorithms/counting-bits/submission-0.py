class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for n in range(n + 1):
            # inner while loop to calculate amount of 1s in this number
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1

                n = n >> 1

            output.append(count)

        return output