class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequencies = defaultdict(int)
        max_window_length = 0
        most_frequent_char = None

        left, right = 0, 0
        while right < len(s):
            # Calculating window length and most frequent character
            char = s[right]
            frequencies[char] += 1
            most_frequent_char = char if frequencies[char] > frequencies[most_frequent_char] else most_frequent_char
            window_length = right - left + 1

            # Update sliding window
            if window_length - frequencies[most_frequent_char] <= k:
                right += 1
                max_window_length = max(window_length, max_window_length)
            else:
                left += 1
                frequencies[left-1] -= 1

        return max_window_length