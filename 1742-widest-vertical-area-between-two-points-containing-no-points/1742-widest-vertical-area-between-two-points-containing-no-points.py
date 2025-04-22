class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        #Extract the x-values from all points
        x_vals = [x for x, y in points]

        x_vals.sort()

        max_width = 0
        for i in range(1,len(x_vals)):
            max_width = max(max_width, x_vals[i] - x_vals[i-1])

        return max_width