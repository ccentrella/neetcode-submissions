class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Store s1 values in dictionary to account for all permutations
        s1_chars = defaultdict(int)
        for char in s1:
            s1_chars[char] += 1

        # Verify dictionary items exist sequentially in s2
        left, right = 0, 0
        while right < len(s2):
            if len(s1_chars) == 0:
                return True

            if s2[right] in s1_chars:
                s1_chars[s2[right]] -= 1
                if s1_chars[s2[right]] == 0:
                    del s1_chars[s2[right]]
                right += 1
            else:
                s1_chars[s2[left]] += 1
                left += 1

        # If we reach this point no permutation exists in s2
        return False
