class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        if len(set(freq.values())) == len(freq.values()):
            return True
        else:
            return False
