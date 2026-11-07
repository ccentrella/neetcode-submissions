class Solution:
    # One option: Sort these and confirm both are the same
    # However, this requires converting to list so it takes O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths do not match, it cannot be a valid anagram
        if len(s) != len(t):
            return False

        list_s = [char for char in s]
        list_t = [char for char in t]

        # Sort the lists
        list_s = sorted(s)
        list_t = sorted(t)

        # Now confirm the lists match
        for index in range(len(s)):
            # If one does not match, it is not an anagram
            if list_s[index] != list_t[index]:
                return False

        # If we reach here, everything matches and it is a valid anagram
        return True