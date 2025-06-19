class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
        
        if not freq:
            return -1

        max_freq = max(freq.values())

        candidates = [num for num in freq if freq[num] == max_freq]

        return min(candidates)