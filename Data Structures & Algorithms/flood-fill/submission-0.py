class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # If the color is the same as the target, then return the image, because it is already in right format
        initial_color = image[sr][sc]
        if initial_color == color:
            return image

        # Now start the traversal
        return self.fillNeighbors(image, sr, sc, initial_color, color)

    def fillNeighbors(self, image: List[List[int]], sr: int, sc: int, old_color: int, new_color:int) -> List[List[int]]:
        # Base case: Ignore if out of bounds
        if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0])):
            return image

        # Base case: Ignore if color is wrong
        if image[sr][sc] != old_color:
            return image

        # Base case: Update with new color
        image[sr][sc] = new_color

        # Update four positions
        self.fillNeighbors(image, sr+1, sc, old_color, new_color)
        self.fillNeighbors(image, sr, sc+1, old_color, new_color)
        self.fillNeighbors(image, sr-1, sc, old_color, new_color)
        self.fillNeighbors(image, sr, sc-1, old_color, new_color)

        return image