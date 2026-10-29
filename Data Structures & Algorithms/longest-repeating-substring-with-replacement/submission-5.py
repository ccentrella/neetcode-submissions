class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        max_window_length, max_frequency = 0, 0

        left = 0
        for right in range(len(s)):
            frequencies[s[right]] += 1
            max_frequency = max(max_frequency, frequencies[s[right]])
            window_length = right - left + 1

            if window_length - max_frequency <= k:
                max_window_length = max(window_length, max_window_length)
            else:
                frequencies[s[left]] -= 1
                left += 1

        return max_window_length