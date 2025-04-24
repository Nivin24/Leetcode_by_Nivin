class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for im in image:
            l, r = 0, len(im) - 1
            while l < r:
                im[l], im[r] = im[r], im[l]
                l += 1
                r -= 1

        for im in image:
            for i in range(len(im)):
                if im[i] == 0:
                    im[i] = 1
                else:
                    im[i] = 0

        return image