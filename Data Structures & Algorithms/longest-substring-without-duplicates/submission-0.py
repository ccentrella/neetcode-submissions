class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        longest_substring = 0
        left, right = 0, 0
        while right < len(s):
            window[s[right]] += 1
            if window[s[right]] > 1 and window[s[left]] == 1:
                del window[s[left]]
                left += 1
            elif window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            else:
                longest_substring = max(longest_substring, len(window))
            right += 1

        return longest_substring