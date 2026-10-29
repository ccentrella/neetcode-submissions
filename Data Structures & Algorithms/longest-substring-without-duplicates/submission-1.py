class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest_substring = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
                longest_substring = max(longest_substring, len(window))
                right += 1
        return longest_substring