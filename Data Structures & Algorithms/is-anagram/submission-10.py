class Solution:
    # An alternative solution is to use a hash map
    # Also takes O(n) space, but only O(n) time
    def isAnagram(self, s: str, t: str) -> bool:

        # Confirm both lists are the same size
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}
        for index in range(len(s)):
            map_s[s[index]] = map_s.get(s[index], 0) + 1
            map_t[t[index]] = map_t.get(t[index], 0) + 1

        # For hashmaps, python compares hash value for equality, not the refernce
        return map_s == map_t