class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequencies = defaultdict(int)
        max_window_length = 0
        most_frequent_char = None

        left, right = 0, 0
        for right in range(len(s)):
            char = s[right]
            frequencies[char] += 1
            most_frequent_char = char if frequencies[char] > frequencies[most_frequent_char] else most_frequent_char
            window_length = right - left + 1

            # Update sliding window
            if window_length - frequencies[most_frequent_char] <= k:
                max_window_length = max(window_length, max_window_length)
            else:
                frequencies[s[left]] -= 1
                left += 1

        return max_window_length