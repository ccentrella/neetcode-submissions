class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = h // len(piles)
        right = max(piles)
        minimum = -1
        while left <= right:
            current_size = (left + right) // 2
            required_hours = sum([math.ceil(pile / current_size) for pile in piles])
            if required_hours <= h:
                minimum = current_size
                right = current_size - 1
            else:
                left = current_size + 1
        return minimum