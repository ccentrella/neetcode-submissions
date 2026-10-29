class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Could use array or dict
        # Iterate over first string and store characters
        # Then match using second string
        # Use dict bc array lookup time is too slow

        # Store characters from s in dictionary
        characters = {}
        for character in s:
            characters[character] = characters.get(character, 0) + 1

        # Remove characters from t
        print(characters)
        for character in t:
            characters[character] = characters.get(character, 0) - 1
        
        for value in characters.values():
            if value != 0:
                return False

        # If we reach this point strings are anagrams of each other
        return True