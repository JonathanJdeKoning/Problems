class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row] = image[row][::-1]
            for bit in range(len(image[row])):
                if image[row][bit] == 1:
                    image[row][bit] = 0
                elif image[row][bit] == 0:
                    image[row][bit] = 1
        return image