class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        actual_color = image[sr][sc]
        return self.recursiveFloodFill(image, sr, sc, color, actual_color)

    def recursiveFloodFill(self, image, sr, sc, color, actual_color):
        if actual_color == color:
            return image
        if (sr < 0 ) or (sr >= len(image)) or (sc < 0) or (sc >= len(image[0])):
            return image
        if image[sr][sc] == actual_color:
            image[sr][sc] = color
            return (self.recursiveFloodFill(image, sr + 1, sc, color, actual_color) and
            self.recursiveFloodFill(image, sr - 1, sc, color, actual_color) and
            self.recursiveFloodFill(image, sr, sc + 1, color, actual_color) and
            self.recursiveFloodFill(image, sr, sc - 1, color, actual_color))
        return image



if __name__=="__main__":
    sol = Solution()
    # print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    print(sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))