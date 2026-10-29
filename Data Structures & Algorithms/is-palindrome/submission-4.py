class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [char.lower() for char in s if char.isalnum()]
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1; right -= 1
        return True