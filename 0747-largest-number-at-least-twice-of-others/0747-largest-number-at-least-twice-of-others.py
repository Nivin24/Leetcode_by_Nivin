class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_num = max(nums)
        max_index = nums.index(largest_num)
        res = 0

        for n in nums:
            if n != largest_num and largest_num < 2 * n:
                return - 1
        return max_index