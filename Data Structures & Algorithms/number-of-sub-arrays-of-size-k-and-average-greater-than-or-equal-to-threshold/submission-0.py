class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Since k is always equal to 3, use sliding window
        # However, we need a way to calculate the average
        # A naive way is to calculate average of each item in window but this would be O(nk) time
        # How we can recalculate average more efficiently by expanding the existing average and swapping the old value with the new value

        running_total = 0
        left = 0
        count = 0
        for right in range(len(arr)):
            running_total += arr[right]

            if right - left >= k:
                running_total -= arr[left]
                left += 1

            # Only calculate average if window is ready
            if right - left < k - 1:
                continue

            avg = running_total / k
            if avg >= threshold:
                count += 1

        return count