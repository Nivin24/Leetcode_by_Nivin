class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        curr_max = max(nums)
        curr_min = min(nums)

        return max(0,curr_max - curr_min - 2 * k)