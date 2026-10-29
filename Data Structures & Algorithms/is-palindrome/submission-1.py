class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)
        while left < right:
            if s[left] != s[right]:
                return False

            # If we reach this point, we have a Palindrome
            return True