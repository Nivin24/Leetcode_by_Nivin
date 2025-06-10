class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_no_rob = 0  
        prev_rob = 0     

        for val in nums:

            new_no_rob = max(prev_no_rob, prev_rob)

            new_rob = prev_no_rob + val

            prev_no_rob, prev_rob = new_no_rob, new_rob

        return max(prev_no_rob, prev_rob)