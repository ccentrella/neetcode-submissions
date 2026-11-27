class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        array = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # If the item matches, use diagnonal next
                    array[i][j] = 1 + array[i+1][j+1]
                else:
                    array[i][j] = max(array[i+1][j], array[i][j+1])

        return array[0][0]

# If characters match, keep traversing diagonally
# Otherwise, get max from traversing horizontally and vertically