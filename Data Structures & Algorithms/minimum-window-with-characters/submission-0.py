class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Use hashmap to record characters in t
        t_chars = defaultdict(int)
        for char in t:
            t_chars[char] += 1

        current_matches = defaultdict(int)
        minimum_substring = None
        left, right = 0, 0
        while right < len(s):
            print(left,right)
            if s[left] not in t_chars:
                left += 1
                self.on_update_pointer(s, left, t_chars, current_matches)
            elif s[right] in t_chars:
                if current_matches == t_chars:
                    print(True,left,right)
                    minimum_substring = s[left:right+1]
                    current_matches[left] -= 1
                    left += 1
                    elf.on_update_pointer(s, left, t_chars, current_matches)
                else:
                    right += 1
            else:
                right += 1

        return minimum_substring

    def on_update_pointer(self, s, index, t_chars, current_matches):
        if s[index] in t_chars:
            current_matches[s[index]] += 1

        

        # After incrementing left or right pointer, need to immediately add item to found list if applicable
        # Can't happen during each loop bc a pointer will be in the same position multiple times

# Find index of first letter in substring and continue until each character is foujnd
# Need to check indices of additional letters as well bc the substring could be shorter
# This means we need to check and potentially update the substring start point each time one of the characters matches
# When a character doesn't match, ignore it.

# First adjust left pointer until first index is found
# Then adjust right pointer until entire substring is found