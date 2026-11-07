class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # The prefix cannot be longer than any of the words
        # So we can start off by setting to the first word
        # At each iteration, once we find a character that is not the same, then we stop

        # First, ensure the string is not empty
        if not strs:
            return ""

        prefix = strs[0]
        
        # Have a loop in here to iterate over each character
        # Notice that this is still O(n) time, or at least O(wn), but w is the length
        #  of the longest word so we can think of it as a constant
        for str in strs:
            # The prefix cannot be longer than any of the words
            if len(prefix) > len(str):
                prefix = prefix[:len(str)]

            for index in range(len(str)):
                # If the string is longer and we reach until the end, the prefix still holds
                if index >= len(prefix):
                    break

                # If these don't match, we update and also break
                if prefix[index] != str[index]:
                    prefix = prefix[:index]

        return prefix
            
        # Space: O(1)
        # Time: O(n)