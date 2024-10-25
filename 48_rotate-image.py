class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # O(n^2) time, O(1) space
        # where n is side length of square
        
        # rotate image in layers, starting from outside to inside until 1x1 square reached
        l = 0
        r = len(matrix) - 1

        while l < r:
            # for each layer, move each corner of square clockwise
            # repeat for all possible squares in layer
            for i in range(r - l):
                top = l
                bot = r
                topLeft = matrix[top][l + i]

                # move bottom left to top left
                matrix[top][l + i] = matrix[bot - i][l]

                # move bottom right to bottom left
                matrix[bot - i][l] = matrix[bot][r - i]

                # move top right to bottom right
                matrix[bot][r - i] = matrix[top + i][r]

                # move top left to top right
                matrix[top + i][r] = topLeft

            # shrink to next layer
            l += 1
            r -= 1